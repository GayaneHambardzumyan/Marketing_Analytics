# Bass Model Homework: Fujifilm instax WIDE Evo

Diffusion analysis of the **Fujifilm instax WIDE Evo** hybrid instant camera (from TIME's 2025 Best Inventions list) using the Bass diffusion model, with the **digital still camera** as the look-alike innovation.

Author: Gayane Hambardzumyan 

## Summary

- **Look-alike:** digital still cameras, worldwide shipments 1999-2025 (CIPA, 2025).
- **Estimated Bass parameters (look-alike):** p = 0.0100, q = 0.3813, M ≈ 1.2 billion units, R² = 0.969.
- **Market potential for the Evo (Fermi estimate):** 100 million instax units x 10% WIDE share x 30% hybrid share = 3 million units. The two shares are assumptions.
- **Scope:** global.
- **Forecast (2025-2039):** annual adoption peaks in 2035 at about 299 thousand units; cumulative adopters reach about 2.6 million (87% of M) by 2039.

The full analysis is in [`report/report.pdf`](report/report.pdf).

## Repository structure

```
Bass_Model/
├── README.md
├── DS223_hw1_Gayane_Hambardzumyan.ipynb   # full analysis (code, outputs, comments)
├── data/
│   ├── cr300.pdf                          # CIPA source file
│   ├── cipa_shipments.csv                 # extracted shipments (thousand units)
│   └── evo_adopters_forecast.csv          # Evo forecast by year
├── img/
│   ├── image1.png                        # Bass fit to digital camera shipments
│   └── image2.png                   # Evo annual and cumulative adopters
├── report/
│   ├── report.pdf                         # final report
│   └── report_source.md                   # markdown source of the report
├── /:
│   ├── helper_functions.py                #Bass model function        
│   └── extract_cipa_data.py              #converts the CIPA pdf (cr300.pdf) into data/cipa_shipments.csv
│   ├── estimate_bass.py                  #estimates p, q, M for digital still cameras    
│   └── forecast_evo.py                   #forecasts the diffusion of the Instax Wide Evo
```

## How to run

1. Install the dependencies provided in the 'imports' cell of the notebook
2. Open the notebook in Jupyter or Google Colab and run all cells. The notebook asks you to upload a file. Upload `cr300.pdf` (in `data/`). The notebook parses the shipments table from it.

## References

- Camera & Imaging Products Association (CIPA). (2025). *Total shipments of digital still cameras (classified by type).* https://www.cipa.jp/stats/documents/common/cr300.pdf
- Fujifilm. (2025, January 21). *instax WIDE Evo hybrid instant camera.* https://www.fujifilm.com/fi/en/news/Fujifilm-introduce/instax-WIDE-Evo-Hybrid-Instant-Camera
- Fujifilm Corporation. (2025, April 8). *instax cumulative sales exceeds 100 million units.* https://www.fujifilm.com/jp/en/news/hq/12295
