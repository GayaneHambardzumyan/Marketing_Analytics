---
title: 'Innovation Diffusion Analysis: Fujifilm instax WIDE Evo'
author: "Gayane Hambardzumyan"
subtitle: Homework on the Bass Model (DS223)
output: pdf_document
---

## 1. Choice of Innovation

The selected innovation is the **Fujifilm instax WIDE Evo**, a hybrid instant camera from TIME's list of best innovations. It captures images digitally, previews them on a 3.5-inch LCD with lens and film effects applied, stores them in internal memory or on a micro SD card, and prints selected images on instax WIDE film (Fujifilm, 2025a).


## 2. Look-alike Innovation: The Digital Still Camera

I chose the **digital still camera** as the look-alike. 

**Functionality and technology.** Both products combine photography with a digital workflow. The Evo adds a digital sensor, preview screen, memory storage and image selection to instant film. Digital still cameras brought the same core changes to film photography in the late 1990s: an electronic sensor, instant on-screen preview, removable memory, and the freedom to select, edit and share photos instead of committing every frame to film. In both cases a digital imaging pipeline is built into a familiar camera form, and the user value comes from combining a traditional camera experience with digital control.

**Market impact.** The structure of adoption is also comparable. Digital cameras were adopted first by people who already owned film cameras and understood photography, and they spread through word of mouth and visible use. This is the mix of innovation and imitation that the Bass model describes. CIPA's worldwide shipment data show the pattern: shipments grew from about 5.1 million units in 1999 to a peak of about 121.5 million in 2010 (CIPA, 2025). The Evo targets a similar buyer, someone who already values a camera and now gets a digital layer on top. One difference is that the Evo is a new generation within the existing instant-camera category rather than an entirely new product category, so its market is much smaller.

## 3. Historical Data

The time series is the worldwide annual shipments of digital still cameras for 1999–2025, published by the Camera & Imaging Products Association (CIPA, 2025). The table in the CIPA PDF was parsed with `pdfplumber`, and the result was saved to `data/cipa_shipments.csv` (27 observations, in thousands of units).

## 4. Estimation of Bass Model Parameters

The Bass model in discrete form is

$$S(t) = pM + (q-p)\,N(t-1) - \frac{q}{M}\,N(t-1)^2,$$

where $S(t)$ is sales in period $t$, $N(t-1)$ is cumulative sales before $t$, $p$ is the coefficient of innovation, $q$ is the coefficient of imitation and $M$ is the market potential. The parameters were estimated by nonlinear least squares (`scipy.optimize.curve_fit`) with starting values $p=0.01$, $q=0.4$, $M=1{,}200{,}000$ (thousand units).

| Parameter | Estimate |
|---|---:|
| $p$ | 0.0100 |
| $q$ | 0.3813 |
| $M$ | 1,195,308 thousand units (about 1.2 billion) |
| $R^2$ | 0.969 |


**Interpretation.** The model fits the data well ($R^2 = 0.969$). Because $p$ is small, few buyers adopted independently of others. Because $q$ is much larger than $p$ (about 38 times), diffusion was driven mainly by imitation and word of mouth. $M$ is the estimated lifetime market of about 1.2 billion cameras. 

## 5. Predicting the Diffusion of the instax WIDE Evo

**Parameters.** The look-alike coefficients $p = 0.01$ and $q = 0.38$ are applied to the Evo. Only $M$ must be adapted, because the Evo's market is far smaller than the digital camera market.

**Market potential (Fermi estimate).**

$$M_{Evo} = 100\text{ million} \times 10\% \times 30\% = 3\text{ million units}$$

- 100 million: cumulative instax film-camera units sold worldwide (Fujifilm, 2025b).
- 10%: assumed share of the WIDE format among instax cameras (assumption).
- 30%: assumed share of hybrid, Evo-type models within the WIDE format (assumption).

The 10% and 30% shares are my own assumptions, not sourced figures, and $M$ scales directly with them.

**Setup.** Launch is in 2025 (period 1) and the forecast covers 15 years (2025–2039).

The model predicts slow initial adoption, then accelerating growth driven by imitation, a peak of about 300 thousand adopters per year in 2035–2036, and a decline as the remaining part of potential buyers shrinks.

## 6. Choice of Scope

I analyze diffusion at the **global** level, for three reasons.

1. **The market is international.** Fujifilm describes instax as a global brand available in more than 100 countries and regions (Fujifilm, 2025b), so a single-country analysis would capture only a small part of the market.
2. **The look-alike data is global.** The CIPA shipments used to estimate $p$ and $q$ are worldwide (CIPA, 2025). A global forecast keeps the scope consistent between the look-alike and the new product.
3. **The market potential is built from global data.** The $M$ estimate starts from Fujifilm's worldwide cumulative instax sales, which are not published by country (Fujifilm, 2025b).

## 7. Number of Adopters by Period

**Key findings.**

- Adoption starts slowly, with about 30 thousand adopters in 2025 and about 100 thousand per year by 2029.
- Annual adoption peaks in 2035 at about 299 thousand units, then declines to about 182 thousand by 2039.
- Cumulative adopters reach about 2.6 million by 2039, which is 87% of the assumed market potential.
- The shape is driven mostly by word-of-mouth imitation ($q = 0.38 \gg p = 0.01$), as it was for digital still cameras.
- The timing of the peak depends on $p$ and $q$ only; the size of the adopter counts scales with the assumed $M$.


## References

Camera & Imaging Products Association (CIPA). (2025). *Total shipments of digital still cameras (classified by type)*. https://www.cipa.jp/stats/documents/common/cr300.pdf

Fujifilm. (2025a, January 21). *instax WIDE Evo hybrid instant camera*. https://www.fujifilm.com/fi/en/news/Fujifilm-introduce/instax-WIDE-Evo-Hybrid-Instant-Camera

Fujifilm Corporation. (2025b, April 8). *instax cumulative sales exceeds 100 million units*. https://www.fujifilm.com/jp/en/news/hq/12295
