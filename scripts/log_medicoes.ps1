<# 
log_medicoes.ps1
Script interativo para registrar medições da Ficha_Medicoes.xlsx em CSV.
Requisitos: PowerShell 5+
#>

param(
    [string]$PlanilhaXlsx = "../forms/Ficha_Medicoes.xlsx",
    [string]$SaidaCsv = "../forms/Ficha_Medicoes_log.csv"
)

Write-Host "=== Registro de Medições (CFTV Analógico) ==="

function Prompt-Value($label) {
    Read-Host ($label + ":")
}

$registro = [ordered]@{
    Data = (Get-Date).ToString("yyyy-MM-dd HH:mm")
    Tecnico = Prompt-Value "Técnico"
    CameraID = Prompt-Value "CameraID"
    Ponto = Prompt-Value "Ponto (local)"
    ComprimentoEstimado_m = Prompt-Value "Comprimento estimado (m)"
    Cont_Malha_Ohm = Prompt-Value "Continuidade malha (Ohm)"
    Cont_Centro_Ohm = Prompt-Value "Continuidade condutor central (Ohm)"
    Isolacao_MOhm = Prompt-Value "Isolação (MΩ) com 250–500 V"
    DP_Terras_VDC = Prompt-Value "Diferença de potencial de terras (VDC)"
    DP_Terras_VAC = Prompt-Value "Diferença de potencial de terras (VAC)"
    "Osc_Picos(Yes/No)" = Prompt-Value "Osciloscópio: picos/transientes? (Yes/No)"
    "Ondul_50_60Hz(Yes/No)" = Prompt-Value "Ondulação 50/60 Hz? (Yes/No)"
    Observacoes = Prompt-Value "Observações"
    "Status(Antes/Depois)" = Prompt-Value "Status (Antes/Depois)"
}

# Salva/Acumula no CSV
$exists = Test-Path $SaidaCsv
$registro.GetEnumerator() | Out-Null
$line = ($registro.Keys | ForEach-Object { $registro[$_] }) -join ","

if (-not $exists) {
    ($registro.Keys -join ",") | Out-File -FilePath $SaidaCsv -Encoding UTF8
}
$line | Out-File -FilePath $SaidaCsv -Append -Encoding UTF8

Write-Host "Registro salvo em $SaidaCsv"
