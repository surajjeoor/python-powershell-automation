import json

def save_experiment_results(file_path, results):
    """
    Save experiment results to a JSON file.

    :param file_path: Path to the JSON file.
    :param results: Dictionary containing experiment results.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

def json_file_reader(file_path):
    """
    Read experiment results from a JSON file.

    :param file_path: Path to the JSON file.
    :return: Dictionary containing experiment results.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Example usage
experiment_results = {
    'experiment_1': {
        'accuracy': 0.95,
        'loss': 0.05,
        'parameters': {
            'learning_rate': 0.001,
            'batch_size': 32
        }
    },
    'experiment_2': {
        'accuracy': 0.92,
        'loss': 0.08,
        'parameters': {
            'learning_rate': 0.01,
            'batch_size': 64
        }
    }
}
save_experiment_results('experiment_results.json', experiment_results)
loaded_results = json_file_reader('experiment_results.json')
print(loaded_results)