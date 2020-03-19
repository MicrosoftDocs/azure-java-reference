# Assumptions
#   This script is being executed in the MicrosoftDocs/azure-java-reference repository
#   This script is running on at least python 2.7



Get-Content "unified-latest/reference-latest.yml","legacy-docs-toc-merge/toc.yml" | Set-Content "univied-latest/reference-latest.yml" 