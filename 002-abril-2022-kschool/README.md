# Abril 2022 - 📈 Machine learning en producción y explicabilidad algorítmica

- **Evento**: https://www.meetup.com/PyData-Madrid/events/284942321/
- **Grabación**: N/A
- **Fotos**: https://www.meetup.com/PyData-Madrid/photos/32262340/


### Nota con respecto a las exploraciones de la charla de NannyML

- Durante la charla de NannyML se realizo la exploracion con un caso de uso real y se presentaron los desafios del chunk automatico con respecto a los datos de la particion de analisys. Al intercambiar los resultados con los creadores de la libreria se descubrio la posibilidad de que los **objetos datetime no estuvieran ordenados** y que por tanto esto tuviese un impacto en el chunk automatico a la hora de declarar el CBPE. La posibilidad de que ahora funcione con objetos datetimes no ordenados fue incluida en el [Fixed](https://github.com/NannyML/nannyml/releases/tag/v0.3.2) de la libreria.
