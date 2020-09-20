# Guia-ROS
Esta actividad se verá orientada a estudiantes de la materia Fundamentos de Robótica Móvil, donde se contará con una serie de vídeos explicativos (tipo tutorial), referente a cada una de las unidades vistas en la guía que se presentará más adelante. El formato de entrega de la guía será por medio de carpetas, aquellas estarán divididas dependiendo la unidad y al final se adjuntará un taller en el cual se ponga en práctica toda la información aprendida en el mismo. Los entregables para este proyecto serán una serie de vídeos tutoriales, repositorio en GitHub( Códigos, pre-requisitos, Readme) y guía de trabajo anteriormente especificada.

## Pre-resquisitos
- Ubuntu instalado (aconsejable versión 16.04 o 18.04)
- ROS, Gazebo y Turtlebot 3 instalados (aconsejable Melodic o kinetic)
- Conocimientos básicos de Python y CommandWindow de Ubuntu

### Tutoriales de instalación de los pre-requisitos
- ubuntu:https://ubunlog.com/guia-de-instalacion-de-ubuntu-18-04-lts-bionic-beaver/#:~:text=Proceso%20de%20instalaci%C3%B3n-,Requisitos%20para%20instalar%20Ubuntu%2018.04%20LTS,puerto%20USB%20para%20la%20instalaci%C3%B3n.
- ROS: http://wiki.ros.org/melodic/Installation/Ubuntu
- Gazebo: http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install
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
### Instalación del gazebo
1. Para la correcta instalación del Gazebo se debe accder y seguir los pasos del siguiente repositorio: http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install
2. Luego de la instalación solo resta abrirlo con el comando `roslaunch turtlebot3_gazebo`

## UNIDAD III - Husky
En esta unidad se expondrán las características que tiene uno de los robots móviles más conocidos actualmente que emplean la configuración Skid Steer, ampliaremos la información hacia el mundo de ROS y explicaremos brevemente como se da la instalación de su simulación y que sensores trae implementada su versión digital.
### Instalación del simulador del Husky en Gazebo (ROS melodic)
1. `sudo apt install ros-melodic-desktop`
2. `sudo apt install ros-melodic-simulator`
### Correr los mundos instalados con el Husky
- Mundo vacío `roslaunch husky_gazebo husky_empty_world.launch`
- Mundo con distintos elementos y variaciones en cuanto a suelo ` roslaunch husky_gazebo husky_playpen.launch`
## UNIDAD IV - Control remoto
En esta unidad se describirá y explicará paso a paso como podemos enlazar correctamente un mando con el Gazebo y a su vez se mostrará como realizar la conexión de este con el robot que se ecuentre siendo simulado en el space de Gazebo.
### Instalación y reconocimiento del control
1. Escribimos la linea de código dependiendo de nuestra versión de ROS `sudo apt install ros-melodic-joy`
2. Sin conectar el control escribimos la instrucción `ls /dev/input/`
3. Al conectar nuestro control ejecutamos la misma instrucción para así saber cual es el puerto al que se enlasa este `ls /dev/input/`
4. Se crea un archivo punto sh con `nano inicioControl.sh`
5. Luego en el archivo se copia
```
#!/bin/bash
# -*- ENCODING: UTF-8 -*-

echo "Configuracion mi control"

sudo chmod a+rw /dev/input/jsx
echo "2"
rosparam set joy_node/dev "/dev/input/jsx"
rosrun joy joy_node
```
6. Al guardar el archivo anterior ejecutamos la instrucción `roscore`
7. Ejecutamos el archivo guardado anteriormente con la instrucción `bash inicioControl.sh`
### Controlar los movimiento del Turtlebot 3 con el control
1. Para realizar la conexión simplemente se debe crear un archivo en python con `nano escuhjoyXBOXprofesor.py`
2. Cuando el roscore esté corriendo es necesario correr el código (se encontará disponible en el src de la unidad 4) `python escuhjoyXBOXprofesor.py`
3. Abrir el gazebo con el turtlebot 3 `roslaunch turtleblo3_gazebo turtlebot3_world.launch`
4. Para nuestro código (XBOX 360) se debe avanzar con el análogo derecho y dar giro con el izquierdo, esto solo funciona cuando LB esté presionado.
## UNIDAD V - Aplicación del celular 
Para llevar a cabo esta unidad se presentará un video explicativo en donde se evidencie todo lo relacionado con la aplicación, desde como instalarla hasta como utilizarla.
1. Se debe descargar la aplicación de android llamada ros all sensors drive 
2. Buscar la dirección IP del ordenador por medio de la aplicación angry IP scanner
3. Copiar la siguiente línea de código en la consola, reemplazando el número por la IP correspondiente de cada ordenador
```
export ROS_MASTER_URI=http://192.168.1.8:11311/
```
4. Se inicia el roscore en el CommandWindow
5. Se verifica que la información sea correcta corriendo las siguientes líneas de código
```
rostopic list 
rostopic echo /phone1/android/imu
```

