$EventFilterName = 'calcSpawned'
$EventConsumerName = 'launchPowerShell'

$EventConsumerToCleanup = Get-WmiObject -Namespace root/subscription -Class CommandLineEventConsumer -Filter "Name = '$EventConsumerName'"
$EventFilterToCleanup = Get-WmiObject -Namespace root/subscription -Class __EventFilter -Filter "Name = '$EventFilterName'"
$FilterConsumerBindingToCleanup = Get-WmiObject -Namespace root/subscription -Query "REFERENCES OF {$($EventConsumerToCleanup.__RELPATH)} WHERE ResultClass = __FilterToConsumerBinding"

# Clean up Code - Comment this code out when you are installing persistence otherwise it will be removed
$FilterConsumerBindingToCleanup | Remove-WmiObject
$EventConsumerToCleanup | Remove-WmiObject
$EventFilterToCleanup | Remove-WmiObject