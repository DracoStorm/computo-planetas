
  # Proyecto Simulación de Planetas


### ITI BUAP - Computo Distribuido


El objetivo es simular el sistema solar con un _computo_ que permita obtener orbitas estables semejantes a las reales, para ser animadas con imágenes estáticas extraidas de archivos _gif_ las cuales cambian frame por frame para ser suavizadas por un _filtro convolucional_ en un **sistema distribuido**.

Se utilizan las siguientes fórmulas en los cálculos:

_Distancia:_
$$
    d=\sqrt{(x_1 - x_2)² + (y_1 - y_2)²+(z_1 - z_2)²}
$$
_Atracción gravitacional:_
$$
    \vec{F}=G\frac{m_1 m_2}{d²}
$$


![gif sistema solar](https://static.wixstatic.com/media/101f43_6bd88c3244054dbf80576270bad01779~mv2.gif "Ejemplo de animacion del sistema")