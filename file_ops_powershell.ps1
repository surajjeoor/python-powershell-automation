$content=Get-Content -Path "C:\Users\sjeoo\projects_Nov2025\experiment_results.json"

'experiment_3: {
        "accuracy": 0.95,
        "loss": 0.05,
        "parameters": {
            "learning_rate": 0.01,
            "batch_size": 64
        }
    }' | Set-Content -Path "C:\Users\sjeoo\projects_Nov2025\experiment_results.json"

    Rename-Item -Path "C:\Users\sjeoo\projects_Nov2025\experiment_results.json" -NewName "experiment_results_updated.json"