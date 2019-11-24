# BaseData

- Простая программа написана с использованием библиотеки `tkinter`
- И вторая библиотека `sqLite3`
- Есть 4 поля **Название**, **Автор**, **Магазин**, и **Цена**
- `4 кнопки` 
    + добавить товар
    + удалить товар
    + изменить товар
    + стереть товар
 - И `ListBox` - куда выводится вся информация из базы данных


## Как скомлировать *Py to EXE*? 
    
Нужно установить библиотеку  **Pyinstaller**  (GitHub).

	pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
Дальше заходим в директорию с прогрммой пример `main.py`
   И пишем в cmd `pyinstaller --windowed -F main.py`
   
`-F` Флаг отвечает за то чтобы не было лишних файлов с .exe 

`--windowed`Флаг отвечает за то чтоб при запуске программы не было консоли
    
И программу для упаковки .exe в installer   **NSIS**

	https://sourceforge.net/projects/nsis/ 

В этой программе выбираем `Installer based on .ZIP file` - Нужно то что мы хотим упаковать в inataller запокавать в **zip архив**.


### Screenshot

[DataBase 1](https://i.imgur.com/p0GcQNG.png "DataBase 1")

[DataBase 2](https://i.imgur.com/sdJbvXX.png "DataBase 2")

[DataBase 3 ERROR](https://i.imgur.com/E1dW31j.png "DataBase 3 ERROR")


