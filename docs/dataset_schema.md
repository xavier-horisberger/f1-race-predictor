# Dataset ML (bozza)

Grana: **1 riga = 1 pilota iscritto a 1 gara**. Chiave candidata: (`season`, `round`, `driver_id`).

| Colonna | Ruolo | Note |
|---|---|---|
| season | contesto | anno della stagione |
| round | contesto | identificativo gara nel campionato |
| race_date | ordinamento | usato per split temporale |
| driver_id | identificatore | codice pilota stabile |
| constructor_id | contesto | team attuale alla data del GP |
| circuit_id | contesto | circuito |
| grid_position | feature | solo per modello post-qualifica; griglia ufficiale nota |
| driver_form_5 | feature | media risultati delle **5 gare precedenti**, mai quella corrente |
| team_form_5 | feature | statistiche team prima del GP |
| quali_gap_pct | feature | solo se disponibile prima del GP |
| finish_position | target regressione | gestire DNFs e piazzamenti non classificati |
| is_podium | target classificazione | 1 se posizione finale 1-3, altrimenti 0 secondo policy esplicita |
| status | outcome | distingue finish, ritiro, squalifica, ecc. |

**Attenzione:** non utilizzare `finish_position`, `status` o `is_podium` tra le feature. I valori meteo *reali* della gara non devono essere usati per previsioni pre-gara. Le feature mancanti storicamente non vanno inventate.
