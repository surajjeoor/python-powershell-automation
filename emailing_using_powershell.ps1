$EmailFrom = "sjeoor@outlook.com"
$EmailTo = "mansh.suthar@gmail.com"
$Subject = "Test Email from PowerShell"
$Body = "This is a test email sent using PowerShell script."
$SMTPServer = "smtp.office365.com"
$SMTPCLient = New-Object Net.Mail.SmtpClient($SMPPServer, 587)
$SMTPCLient.EnableSsl = $true
$SMTPCLient.Credentials = New-Object System.Net.NetworkCredential($EmailFrom, "YourPasswordHere")
$SMTPCLient.Send($EmailFrom, $EmailTo, $Subject, $Body)
Write-Output "Email sent successfully to $EmailTo"

# Webscraping part (example)
$response = Invoke-WebRequest -Uri "https://www.example.com"
$parsedHtml = $response.ParsedHtml
$elements= $parsedHtml.getElementsByTagName("a") # Get all anchor tags
foreach ($element in $elements) {
    Write-Output $element.href
}

