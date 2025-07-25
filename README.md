# CollectionFC

A simple collection forecasting library for Python.

## Features
- 7x7 transition matrix estimation
- 12-month cash-flow forecast
- Basic accuracy diagnostics
- CLI interface for easy use
- Jupyter notebook examples

## Quick Start

### Install
```bash
pip install collection-fc
```

### Basic Usage
```bash
python -m collection_fc --mode simple --input ledger.csv
```

### Jupyter Notebooks
Check out the interactive examples in the `examples/` directory:
- `quick_start.ipynb` - Get started in 5 minutes
- `collection_forecasting_demo.ipynb` - Comprehensive demo with visualizations

## Documentation

- **[Minimal Documentation](https://yourusername.github.io/collection_forecasting/minimal.html)** - Clean, focused docs
- **[Full Documentation](https://yourusername.github.io/collection_forecasting/)** - Complete user guide and API reference
- **[Examples](https://yourusername.github.io/collection_forecasting/examples.html)** - Use cases and scenarios

## Advanced Usage

Optional output paths:
```bash
python -m collection_fc --mode simple \
    --input raw/ledger_may25.csv \
    --forecast_path out/fc.csv \
    --matrix_path out/P.csv \
    --validation_path out/val.json
```

## Input Format

Your CSV file should have these columns:

| Column | Type | Description |
|--------|------|-------------|
| `account_id` | string | Unique account identifier |
| `as_of_date` | YYYY-MM-DD | Month-end snapshot date |
| `dpd` | integer | Days past due |
| `balance` | float | Outstanding principal |
| `recovery_amt` | float | Cash collected during month |

## Output Files

- `forecast.csv` - 12-month cash flow projections
- `transition_matrix.csv` - 7×7 state transition probabilities  
- `validation.json` - Model accuracy metrics

## Development

### Install (development mode)
```bash
pip install -e .
```

### Run tests
```bash
python -m pytest
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

---

See `simple_collection_forecasting_library.md` for full documentation.
