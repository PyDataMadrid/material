# Abril 2022 - 📈 Machine learning en producción y explicabilidad algorítmica

- **Evento**: https://www.meetup.com/PyData-Madrid/events/284942321/
- **Vídeo**: N/A
- **Fotos**: https://www.meetup.com/PyData-Madrid/photos/32262340/


### Nota con respecto a las exploraciones de la charla de NannyML

- Durante la charla de NannyML, se realizó la exploracion con un caso de uso real y se presentaron los desafíos del *chunk* automatico con respecto a los datos de la particion de análisis. Al intercambiar los resultados con los creadores de la librería se descubrió la posibilidad de que los **objetos `datetime` no estuvieran ordenados** y que por tanto esto tuviese un impacto en el *chunk* automático a la hora de declarar el CBPE. La posibilidad de que ahora funcione con objetos `datetime` no ordenados fue incluida en el [Fixed](https://github.com/NannyML/nannyml/releases/tag/v0.3.2) de la librería.
