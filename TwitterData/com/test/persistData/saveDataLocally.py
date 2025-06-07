import csv

class SaveCSVData:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_data(self, data):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["created_at", "author_id", "text"])

            for tweet in data.get("data", []):
                writer.writerow([tweet["created_at"], tweet["author_id"], tweet["text"]])
        print(f"\n✅ Tweets saved to: {self.file_path}\n")
            

    def read_data(self):
        with open(self.file_path, 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]