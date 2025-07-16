# CollectionFC ― *Simple Mode* Documentation

Version 0.1

---

## 1 · Purpose

A single‑command workflow that converts a raw collections ledger into:

* A 7×7 transition matrix
* A 12‑month cash‑flow forecast
* Basic accuracy diagnostics

Opinionated defaults keep the interface friction‑free; there are **no tunable parameters** other than file paths.

---

## 2 · Directory & File Layout

```
project/
├── ledger.csv              # input provided by user
├── forecast.csv            # generated cash curve
├── transition_matrix.csv   # generated P‑matrix
└── validation.json         # generated diagnostics
```

---

## 3 · Required Input Schema (`ledger.csv`)

| column         | dtype        | description                       |
| -------------- | ------------ | --------------------------------- |
| `account_id`   | string       | unique account key                |
| `as_of_date`   | *YYYY‑MM‑DD* | month‑end snapshot date           |
| `dpd`          | int          | days past due (raw integer)       |
| `balance`      | float        | outstanding principal at snapshot |
| `recovery_amt` | float        | cash collected during the month   |

Only these five columns are parsed; extra columns are ignored.

---

## 4 · Processing Pipeline

| step | function                      | description                                              | hard‑coded choice            |
| ---- | ----------------------------- | -------------------------------------------------------- | ---------------------------- |
| 1    | `read_csv(path)`              | type‑checks & loads ledger                               | CSV only                     |
| 2    | `assign_state(dpd)`           | maps `dpd` to buckets                                    | grid = 0/30/60/90/120/150/WO |
| 3    | `fit_simple(df, lookback=24)` | counts transitions for most‑recent 24 months and forms P | no smoothing                 |
| 4    | `build_c_vector(df)`          | mean recovery per start‑state                            | arithmetic mean              |
| 5    | `simulate_cash(P,B0,c,H=12)`  | projects cash & balances 12 months                       | fixed horizon                |
| 6    | `write_matrix(P)`             | emits `transition_matrix.csv`                            | always on                    |
| 7    | `write_forecast(curve)`       | emits `forecast.csv`                                     | always on                    |
| 8    | `validate_simple(df,P,c)`     | back‑tests last 12 months                                | emits `validation.json`      |

---

## 5 · Outputs

### 5.1 Transition Matrix (`transition_matrix.csv`)

CSV, 7 × 7. Header row and first column contain state labels `C0‒C5, WO`. Probabilities rounded to 6 dp.

### 5.2 Cash‑Flow Forecast (`forecast.csv`)

\| month (int) | expected\_cash (float) | expected\_balance (float) |

Rows 1 through 12 correspond to forward months.

### 5.3 Validation (`validation.json`)

```json
{
  "one_step_state_accuracy": 0.87,
  "cash_wmape_12m": 0.064,
  "cumulative_bias": 0.021
}
```

---

## 6 · CLI Usage

```bash
# Simple one‑liner
python -m collection_fc --mode simple --input ledger.csv

# Optional custom file names
python -m collection_fc --mode simple \
    --input raw/ledger_may25.csv \
    --forecast_path out/fc.csv \
    --matrix_path out/P.csv \
    --validation_path out/val.json
```

All outputs default to the current working directory when custom paths are omitted.

---

## 7 · Validation Methodology

1. Re‑estimate matrix on window *t‑25 … t‑13*.
2. Predict state mix for *t‑12 … t*; compare with realised.
3. Metrics:

   * **State accuracy**: exact‑state hit ratio for month *t‑11*.
   * **wMAPE‑12m**: weighted mean abs % error on cash, horizon 12.
   * **Cumulative bias**: total predicted cash ÷ actual cash ‑ 1.

Thresholds are reported, not enforced.

---

## 8 · Extensibility hooks

* `bucket.py` – swap in custom bucket grid.
* `matrix.py::fit_advanced()` – planned upgrade path; keeps same I/O contract.
* `stress.py` (TODO) – macro‑scenario overlays.

---

## 9 · Changelog

* **0.1** – initial simple‑mode release with mandatory matrix output.

---

© 2025 CollectionFC
