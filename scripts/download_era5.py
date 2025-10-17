from pathlib import Path

import cdsapi


def download_one_year(client: cdsapi.Client, year: int, filepath: Path) -> None:
    """Downloads a single year of data"""

    dataset = "reanalysis-era5-single-levels-monthly-means"
    request = {
        "product_type": ["monthly_averaged_reanalysis"],
        "variable": [
            "total_precipitation",
            "convective_precipitation",
            "large_scale_precipitation",
            "precipitation_type",
            "convective_snowfall",
            "large_scale_snowfall",
            "snowfall"
            ],
        "year": [str(year)],
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
            ],
        "time": ["00:00"],
        "data_format": "netcdf",
        "download_format": "unarchived",
        "area": [90, -180, 20, 180]
        }

    client.retrieve(dataset, request).download()


def main():
    ybeg = 1979
    yend = 2025

    outdir = Path.home() / "Data" / 
    client = cdsapi.Client()

    for year in range(ybeg, yend+1):

        filepath = make_filepath(year, outdir)

        download_one_year(client, year, filepath)


if __name__ == "__main__":
    main()



