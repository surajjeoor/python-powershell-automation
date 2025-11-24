$csv=Import-Csv -Path "data.csv"

$csv | ForEach-Object{Write-Output $_}

$data= @(
    @{
        Name="Alice"
        Age=30
        City="New York"
    },
    @{
        Name="Bob"
        Age=25
        City="Los Angeles"
    },
    @{
        Name="Charlie"
        Age=35
        City="Chicago"
    },
    @{
        Name="Diana"
        Age=28
        City="Miami"
    }
)

$data | Export-Csv -Path "output.csv" -NoTypeInformation