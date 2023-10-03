import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': [
            '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_wind',
            '10m_v_component_of_wind', '2m_temperature', 'convective_available_potential_energy',
            'convective_rain_rate', 'mean_convective_precipitation_rate', 'mean_large_scale_precipitation_fraction',
            'mean_large_scale_precipitation_rate', 'mean_sea_level_pressure', 'mean_total_precipitation_rate',
            'surface_pressure', 'total_cloud_cover', 'total_column_cloud_ice_water',
            'total_column_water', 'total_precipitation', 'total_totals_index',
        ],
        'year': '2023',
        'month': '09',
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            60, -40, 10,
            50,
        ],
    },
    'ds_plot.grib')
