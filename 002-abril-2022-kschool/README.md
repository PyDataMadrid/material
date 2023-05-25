# Abril 2022 - 📈 Machine learning en producción y explicabilidad algorítmica

- **Evento**: [https://www.meetup.com/PyData-Madrid/events/284942321/](https://www.meetup.com/PyData-Madrid/events/284942321/)
- **Charlas**:
  - [Gema Parreño](https://github.com/SoyGema), Data Scientist, habló de [NannyML](https://www.nannyml.com/), una herramienta *open source* hecha en Python pensada para monitorizar modelos de machine learning en producción, en especial para el estudio del model decay y data drift.
  - [Paloma Megías](https://www.linkedin.com/in/paloma-m-39075b176/), Data Scientist en el Instituto de Ingeniería del Conocimiento (IIC), trató el tema de la explicabilidad algorítmica, con una breve introducción a los métodos más conocidos y centrándose, sobre todo, en la biblioteca [SHAP](https://shap.readthedocs.io/en/latest/index.html).
- **Vídeo**: N/A
- **Fotos**: [https://www.meetup.com/pydata-madrid/photos/32262340/](https://www.meetup.com/pydata-madrid/photos/32262340/)

### Nota con respecto a las exploraciones de la charla de NannyML

- Durante la charla de NannyML, se realizó la exploracion con un caso de uso real y se presentaron los desafíos del *chunk* automatico con respecto a los datos de la particion de análisis. Al intercambiar los resultados con los creadores de la librería se descubrió la posibilidad de que los **objetos `datetime` no estuvieran ordenados** y que por tanto esto tuviese un impacto en el *chunk* automático a la hora de declarar el CBPE. La posibilidad de que ahora funcione con objetos `datetime` no ordenados fue incluida en el [Fixed](https://github.com/NannyML/nannyml/releases/tag/v0.3.2) de la librería.
