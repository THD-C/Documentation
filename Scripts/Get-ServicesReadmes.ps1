New-Variable -Name "DESTINATION_PATH" -Value "./Docs/Services" -Option ReadOnly -Scope Script -Force
New-Variable -Name "OWNER" -Value "THD-C" -Option ReadOnly -Scope Script -Force
New-Variable -Name "SERVICES" -value @{
    "Frontend"      = @{
        "name" = "Frontend"
        "repo" = "Frontend"
    }
    "Frontend_API"  = @{
        "name" = "Frontend API"
        "repo" = "Frontend_API"
    }
    "DB_Manager"    = @{
        "name" = "DB Manager"
        "repo" = "DB_Manager"
    }
    "Mongo_Manager" = @{
        "name" = "Mongo Manager"
        "repo" = "Mongo_Manager"
    }
    "Order_Service" = @{
        "name" = "Orders Service"
        "repo" = "Order_Service"
    }
    "CoinGecko_API" = @{
        "name" = "Price Manager"
        "repo" = "CoinGecko_API"
    }
    "Postgres"      = @{
        "name" = "Postgres (SQL)"
        "repo" = "Postgres"
    }
    "Mongo"         = @{
        "name" = "Mongo (NoSQL)"
        "repo" = "Mongo"
    }
    "The_THDc_App"  = @{
        "name" = "Application Architecture"
        "repo" = "The_THDc_App"
    }
} -Option ReadOnly -Scope Script -Force


function Invoke-Main {
    foreach ($service in $SERVICES.Keys) {
        $RepoName = $SERVICES.$service.repo
        $UrlToDownload = "https://raw.githubusercontent.com/$OWNER/$RepoName/main/README.md"
        $LocalPath = "$DESTINATION_PATH/$RepoName.md"
        try {
            Invoke-WebRequest -Uri $UrlToDownload -OutFile $LocalPath
            Add-LinkToRepo -RepoName $RepoName -MdPath $LocalPath
        }
        catch {
            Write-Host "$($_)"
            Write-Host $UrlToDownload
        }
    }

}
function Add-LinkToRepo {
    param(
        $RepoName,
        $MdPath
    )
    $MD_content = Get-Content -Path $MdPath
    $FirstLine = $MD_content[0]
    $FirstLine = $FirstLine.Replace("#", "").Trim()
    $RepoUrl = "https://github.com/$OWNER/$RepoName"
    $MD_content[0] = "# [$FirstLine]($RepoUrl)"
    $MD_content | Set-Content -Path $MdPath
}

Invoke-Main
