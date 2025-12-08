# variable to store the content of the values
$powerBanks = Get-Content -Path 'd3.txt'

# loops through all the lines in the text file
ForEach ($bank in $powerBanks) {
    # stores the first high value we come across
    $firstHigh = 0;
    # stores the second high value
    $secondHigh = 0;

    # Logic used to find the first high value, we loop through the index of each value in the string comparing them to the last one
    # making sure to stop before the last value in the string. This prevents the last digit from being something like a 9 and thus 
    # not being able fill our second value.
    For ($i = 0; $i -lt $($bank.Length -1); $i++) {
        if ($bank[$i] -gt $firstHigh) {
            $firstHigh = $bank[$i];
        }
    }
    # starts the logic to get the second high value, we start at one point PAST the index of the first high value and can go to the end
    For ($i = $($bank.IndexOf($firstHigh) + 1); $i -lt $bank.Length; $i++) {
        if ($bank[$i] -gt $secondHigh) {
            $secondHigh = $bank[$i];
        }
    }
    # concatenates the value from the firstHigh and secondHigh and stores them as an integer
    $bankTotal = [int]("$firstHigh$secondHigh");
    Write-Host $bankTotal;
    # calcuates the total value based on the current total + the bankTotal for that iteration
    $total += $bankTotal;
}

Write-Host $total;