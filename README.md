# Guia-ROS
Esta actividad se verá orientada a estudiantes de la materia Fundamentos de Robótica Móvil, donde se contará con una serie de vídeos explicativos (tipo tutorial), referente a cada una de las unidades vistas en la guía que se presentará más adelante. El formato de entrega de la guía será por medio de carpetas, aquellas estarán divididas dependiendo la unidad y al final se adjuntará un taller en el cual se ponga en práctica toda la información aprendida en el mismo. Los entregables para este proyecto serán una serie de vídeos tutoriales, repositorio en GitHub( Códigos, pre-requisitos, Readme) y guía de trabajo anteriormente especificada.

## Pre-resquisitos
- Ubuntu instalado (aconsejable versión 16.04 o 18.04)
- ROS, Gazebo y Turtlebot 3 instalados (aconsejable Melodic o kinetic)
- Conocimientos básicos de Python y CommandWindow de Ubuntu

### Tutoriales de instalación de los pre-requisitos
- ubuntu:https://ubunlog.com/guia-de-instalacion-de-ubuntu-18-04-lts-bionic-beaver/#:~:text=Proceso%20de%20instalaci%C3%B3n-,Requisitos%20para%20instalar%20Ubuntu%2018.04%20LTS,puerto%20USB%20para%20la%20instalaci%C3%B3n.
- ROS: http://wiki.ros.org/melodic/Installation/Ubuntu
- Gazebo: 
- TurtleBot3: https://github.com/HaroldMurcia/TurtleBot3_test

## UNIDAD I - Introducción al ROS
En la primera unidad del taller se explicará brevemente la definición del ROS y para que nos ayuda este, también se mencionarán las partes que lo componen así como sus instrucciones principales en el CommandWindow para realizar una determinada acción.
### Comandos principales usados en ROS
- Correr el nodo central o máster `roscore`
- Para ejecutar un nodo específico `rosrun/nombre_del_nodo`
- Ver los nodos disponibles `rosnode list`
- Ver información de los nodos `rosnode info/nombre_del_nodo`
- Ver lista de tópicos disponibles `rostopic list`
- Ver información de los tópicos `rostopic info/nombre_del_topico`
- Visualizar la nformación que envía el tópico `rostopic echo/nombre_del_topico`
- Visualizar la frecuencia de publicación del tópico `rostopic hz/nombre_del_topico`
- Cerrar o finalizar la ejecución de un nodo `rosnode kill/nombre_del_nodo`
- Ver los nodos de una máquina específica `rosnode machin/nombre_de_la_maquina`

## UNIDAD II - GAZEBO
En esta unidad se expondrán las principales funciones del Gazebo, se decribirá como trabaja el programa además de sus principales líneas de código al momentos de implementarlas para abrir los diferentes mundos que este posee.
### Comandos usados en Gazebo
- Para visualizar los mundos disponibles en el Gazebo `roslaunch turtlebot3_gazebo` y luego doble Tap
- Para abrir empty world `roslaunch turtleblo3_gazebo turtlebot3_empty_world.launch`
- Para abrir house `roslaunch turtleblo3_gazebo turtlebot3_house.launch`
- Para abrir world `roslaunch turtleblo3_gazebo turtlebot3_world.launch`
