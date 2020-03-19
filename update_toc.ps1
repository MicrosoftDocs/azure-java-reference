# this should only be run if the generated toc.yml has been updated, otherwise it'll just keep adding duplicates to the build
Param(
  [string]$TargetFolder
)

Write-Host $TargetFolder

$results = Get-Content "$TargetFolder/unified-latest/docs-ref-autogen/toc.yml","$TargetFolder/legacy-docs-toc-merge/toc.yml" 
# needs to be another 
$results | Set-Content "$TargetFolder/unified-latest/docs-ref-autogen/toc.yml" 
Copy-Item -Path "$TargetFolder/legacy-docs-toc-merge/*" -Exclude @("toc.yml") -Destination "$TargetFolder/unified-latest/docs-ref-autogen"

# # converted for main repo
# Param(
#   [string]$TargetFolder
# )

# $results = Get-Content "$TargetFolder/docs-ref-autogen/toc.yml","legacy-docs-toc-merge/toc.yml" 
# # needs to be another 
# $results | Set-Content "$TargetFolder/docs-ref-autogen/toc.yml" 
# Copy-Item -Path "$TargetFolder/legacy-docs-toc-merge/*"  -Destination "$TargetFolder/docs-ref-autogen"
Copy-Item -Force -Path "C:/repo/azure-java-reference/legacy-docs-toc-merge/*"  -Destination "C:/repo/azure-docs-sdk-java/temporary-src-based-yml"


Copy-Item -Force -Path "C:/repo/azure-java-reference/unified-latest/docs-ref-autogen/*"  -Destination "C:/repo/azure-docs-sdk-java/docs-ref-autogen"
Copy-Item -Force -Path "C:/repo/azure-java-reference/unified-preview/*"  -Destination "C:/repo/azure-docs-sdk-java/preview/docs-ref-autogen" 


-Exclude @("toc.yml")