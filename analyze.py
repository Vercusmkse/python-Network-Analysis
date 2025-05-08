import csv
import argparse
from pathlib import Path
import simplegraphs as sg

def main(data_path, output_folder):
    output_folder_path = Path(output_folder)
    output_folder_path.mkdir(parents=True, exist_ok=True)

    with open(data_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        if not reader.fieldnames:
            print("Error: CSV file is empty or headers are missing.")
            return

        rows = list(reader)

        connections = {}
        parents = {}
        siblings = {}

        for row in rows:
            source = row['source'].strip()
            target = row['target'].strip()
            connection_type = row['type'].strip()

            connections[source] = connections.get(source, 0) + 1
            connections[target] = connections.get(target, 0) + 1

            if connection_type == "parent":
                parents.setdefault(target, []).append(source)
            elif connection_type == "sibling":
                siblings.setdefault(source, []).append(target)
                siblings.setdefault(target, []).append(source)

        piblings_count = {user: sum(len(siblings.get(p, [])) for p in parents.get(user, [])) for user in connections}
        niblings_count = {user: sum(len(parents.get(s, [])) for s in siblings.get(user, [])) for user in connections}

        generate_histogram(connections, output_folder_path / "connections.svg", "Total Connections")
        generate_histogram(piblings_count, output_folder_path / "piblings.svg", "Piblings per User")
        generate_histogram(niblings_count, output_folder_path / "niblings.svg", "Niblings per User")

def generate_histogram(data, file_path, title):
    if not data:
        return

    bar_chart_data = [(label, count) for label, count in sorted(data.items(), key=lambda x: x[1], reverse=True)]
    chart_svg = sg.bar_chart(bar_chart_data)
    svg_with_title = sg.svg(800, 400, [sg.text(400, 30, title, size=24), chart_svg])

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_with_title)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze social network data.")
    parser.add_argument("data_path", help="Path to the input CSV file")
    parser.add_argument("-o", "--output-folder", required=True, help="Path to output folder")
    args = parser.parse_args()
    main(args.data_path, args.output_folder)