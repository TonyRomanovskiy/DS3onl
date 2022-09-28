## Результаты тестовых запусков:

В настоящей работе выполнялось чтение страниц с адреса https://en.wikipedia.org
и их сохранение в виде .html файлов на локальном жестком диске (SSD)

Функцонал реализован в виде функций однопоточной (single thread), многопоточной (concurrency) и многопроцессорной (multiprocessing) обработки

Количество потоков/процессов для запуска определялось как количесво логических ЦПУ в системе
CPU_COUNT = os.cpu_count()

### Для тестирования производительности функций выполнялось 3 тестовых прогона: 

#### 1. Запуск №1
There are 0 files in the directory .\files

Running tasks in a single thread:  
task completed in 21.72577929496765 s  
There are 100 files in the directory .\files         

Running tasks in multiple threads (asynchronously):  
task completed in 2.803420066833496 s  
There are 100 files in the directory .\files     

Running tasks in multiple process (separately):  
task completed in 3.269268274307251 s  
There are 100 files in the directory .\files  

#### 1. Запуск №2
There are 0 files in the directory .\files

Running tasks in a single thread:  
task completed in 21.593464851379395 s  
There are 100 files in the directory .\files         

Running tasks in multiple threads (asynchronously):  
task completed in 2.821213722229004 s  
There are 100 files in the directory .\files     

Running tasks in multiple process (separately):  
task completed in 3.158689022064209 s  
There are 100 files in the directory .\files  

#### 1. Запуск №3
There are 0 files in the directory .\files

Running tasks in a single thread:  
task completed in 21.593669176101685 s  
There are 100 files in the directory .\files  

Running tasks in multiple threads (asynchronously):  
task completed in 2.876283884048462 s  
There are 100 files in the directory .\files  

Running tasks in multiple process (separately):  
task completed in 3.250770092010498 s  
There are 100 files in the directory .\files  

## Выводы по результатам тестирования

При взаимодействии с процессами, которые предполагают длительное ожидание ответа, например, реализующими обращения к внешним источникам данных (ЛВС, WEB, БД и пр.) или длительные вычисления,
_Лучшие результаты покажет многопоточная реализация (библиотека concurrent.futures)_

_Многопроцессорная реализация показывает худший результат по отношению к многопоточной_ за счет больших накладных расходов на реализацию, хотя при этом существенно превышает по скорости работы однопоточную.  
Многопроцессорная работа рекомендуется для задач, напрямую зависящих от ЦПУ и оперативной памяти. 

Однопоточная реалиазция показа наихудщее время обработки поставленной задачи.
Однако однопоточность существенно проще в реализации, поддержке и обеспечении стабильной работы приложения.
Не стоит использовать многороточные или многопроцессорные системы без необходимости.