# Precision Agriculture

Model Precision_Agriculture
## SUMMARY

Remote sensing has as one of its objectives, to be able to provide useful information in the shortest possible time for decision-making. Therefore, it is considered a fundamental tool in precision agriculture, since it allows the monitoring of crops throughout the growing season, providing timely information as a diagnostic evaluation. This task must identify the factor that operates in a restrictive manner and decide, in a timely manner, on corrective agronomic intervention.
A promising approach to this is one that integrates data derived from temporal, mosaic, multispectral, and thermal imaging. Both processes allow us to obtain products such as: Thermal maps and Normalized vegetation index maps; These products allow us to identify stress zones which serve as support in agricultural management tasks.
That is why our objective is to develop an Open Source platform, distributed on a GitHub platform that is capable of generating diagnostic tools or early warning of water stress, health status (attack by pests or diseases), phenological status, nutritional deficiencies, productivity. and performance, among others; by capturing the variations in the reflectivity of the plants during the different growth stages, through the processing of images taken with UAV.
Key words: Vegetation index, phenological status, agricultural management, Open Source platform.

## INTRODUCTION

Among the biophysical parameters, the most important ones that can be determined through the use of vegetation index are: ***the chlorophyll content of the leaves (Chl), the leaf area index (LAI) and the Humidity.***
***The chlorophyll content (Chl)*** is an indicator of the ability of the vegetation to carry out photosynthesis, a basic process in the growth and survival of plants and is also directly related to the potencial of plants for the absorption of atmospheric CO2.  
***The leaf area index (LAI)***, its defined as the area of one side of leaves per unit area of soil, provides information on the plant canopy and is a basic parameter for climatic, agronomic and ecological studies.
***The Humidity***, is others bio-indicator of physiological stage of the  plant (health condition and phenology). Plants need a certain amount of moisture to carry out transpiration and other processes.  The transpiration is a processes in which the expel water into the atmosphere through microscopic leaf opening called stomata. As the plant grows, two phenomena occur; turgor and plasmolysis. Turgor is the phenomenon by which cells swell or fill with water and plasmolysis is the opposite process, cells naturally lose water as they wilt. In many cases the response of the vegetation to external aggression such as a disease or to situations of water stress is to increase it temperature.   New remote sensing methods based on high- resolution thermal images have demonstrated their  potential for detecting water stress and estimating photosynthetic performance through detection of fluorescence and chlorophyll activity emitted by vegetation.  
Today the sensors of the cameras on board UAV of capturing spectral in the wavelengths of red, red- edge, near infrared and thermal (Table Nº1).

**Table Nº1:** Multispectral band wavelengths available. 

Multispectral bands
--
| Band | Wavelength |
| -- | -- |
Blue | 450 nm
Green | 560 nm
Red | 650 nm
Red Edge | 730 nm
Near infrared | 840 nm

The following spectral index can be generated from these lengths (Table Nº2).
**Table Nº2:** Spectral index generated from the available wavelengths of camera on board UAV. 

| Índex | Equation |
| -- | -- |
Normalised Difference Index | NDVI = ( Rnir- Rr)/(Rnir+Rr)
Green Normalized Difference Vegetation Index | GNDVI = (Rnir - Rgreen)/(Rnir + Rgreen)
Normalised Difference Red Edge | NDRE = (Rnir - Red edge)/ (Red edge + NIR)
Leaf Chlorophyll Index | LCI = (Rnir - Red edge)/(Rnir + Red)
Optimized Soil Adjusted Vegetation Index | OSAVI = (Nir-Red)/(Nir+Red+0.16)
Enhanced Vegetation Index | EVI = 2.5( Rn- Rr)/ (Rn+ 6*Rr)-(7.5*Rb + 1)*
Leaf area index | LAI= (3.618 x EVI – 0.118) > 0*
Normalized Difference Water Index | NDWI = (Rnir - Swir) / (Rnir + Swir)*


