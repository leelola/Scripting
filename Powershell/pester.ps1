# to runa test
#Invoke-Pester .\pester.ps1

Describe "New_ResourceGroup" {
     $location = 'eastus2'
     $name = 'cloudskillsbootcamp'

It "Name should be clouskillsbootcamp"{
    $name | Should Be 'cloudskillsbootcamp'
}

it "location should be eastus2"{
    $location | Should Be 'eastus2'
}
}