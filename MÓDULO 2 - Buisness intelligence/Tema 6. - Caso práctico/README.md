# Caso práctico
## Se pide
Haciendo uso de PDI, integrar los datos de un informe del CRM Salesforce en la base de datos de prueba.
1. Darse de alta en Salesforce.
2. Descargar el CSV del informe “Activities by Salesperson” a la máquina virtual.
3. Cargar este fichero a la base de datos de pruebas.

## Solución
1. <b>Darse de alta en Salesforce</b>

    Ir a la web de Salesforce y registrarse en la prueba de 30 días.

    Para el registro se deberá dar, por lo menos, un correo electrónico correcto, para poder reiniciar la contraseña.

    <img width="730" height="390" alt="image" src="https://github.com/user-attachments/assets/1df425d0-0146-4b8e-89c0-57caaa105af0" />

    Una vez se tiene acceso al sistema con datos de prueba, se verá la siguiente página y se habrá enviado un correo electrónico para resetear la contraseña.

    <img width="749" height="336" alt="image" src="https://github.com/user-attachments/assets/a09d70e8-1f91-4014-bdf9-8061a2bddcff" />

2. <b>Descargar el CSV del informe Activities by Salesperson a la máquina virtual</b>

    En este caso, seleccionaremos un informe y realizaremos la extracción de datos manual a CSV. Para ello, en el portal, hay que ir a <b>Informes > Todos los informes > Activities by Salesperson</b>.

    <img width="746" height="342" alt="image" src="https://github.com/user-attachments/assets/0c0f90fb-6178-4279-8ff3-c7861516cb36" />

    Se realiza una exportación a CSV.

    <img width="610" height="330" alt="image" src="https://github.com/user-attachments/assets/e91e6351-d399-4467-92ed-cd8b788f56ff" />

    <img width="508" height="368" alt="image" src="https://github.com/user-attachments/assets/04b26aaf-9cc2-4a22-a4aa-f9d738021c15" />

    De esta forma se obtienen los datos de resultados en formato CSV, que posteriormente se pueden integrar de forma automática mediante una herramienta de ETL.

    Como se indicaba antes, aunque este proceso lleva un componente manual, se puede automatizar completamente mediante el uso de los servicios SOAP y herramientas de ETL como PDI.

    <img width="592" height="335" alt="image" src="https://github.com/user-attachments/assets/d207b840-8b85-44f7-ab65-c8dace022bd1" />

3. <b>Cargar este fichero a la base de datos de pruebas</b>

    - Se crea una nueva transformación.
    - Se inserta un paso CSV Input.

      <img width="1211" height="824" alt="image" src="https://github.com/user-attachments/assets/82355c84-a59c-44ba-afa5-9a0781c50cf1" />

    - Se crea la tabla en la base de datos:

      <img width="943" height="718" alt="image" src="https://github.com/user-attachments/assets/e0cf71cd-bb04-4952-8b6a-3589762d616a" />

    - Se crea una conexión a la tabla, reutilizando las conexiones existentes.

      <img width="1164" height="647" alt="image" src="https://github.com/user-attachments/assets/a2a59e53-effe-4370-aa2a-c921556a1be9" />

    - Se establece el mapeo de campos:
  
      <img width="1680" height="645" alt="image" src="https://github.com/user-attachments/assets/e5f36704-3b6a-4512-80e7-fa6dde77e0be" />

    - Y se realiza la carga:
  
      <img width="922" height="783" alt="image" src="https://github.com/user-attachments/assets/9b4e57c7-d4b7-478d-9539-236b10a8f5eb" />
