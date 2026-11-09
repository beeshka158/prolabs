

## Лабораторная работа № 4. Основы работы с системой контроля версий Git и веб-сервисом GitHub.

## Цель работы
Изучить базовые концепции контроля версий, приобрести практические навыки установки и настройки Git, создания локальных и удалённых репозиториев, а также организации структуры для хранения последующих лабораторных работ по программированию.

## Краткие теоретические сведения
Git — это распределённая система контроля версий. Она позволяет фиксировать изменения в файлах (делать «снимки» проекта — коммиты), возвращаться к предыдущим версиям кода и безопасно вести разработку.
Локальный репозиторий — скрытая папка .git на компьютере, где хранится вся история изменений проекта.
Удалённый репозиторий — копия проекта, размещённая на сервере в сети (в данном случае на GitHub). Служит для резервного копирования и демонстрации кода.
Коммит (Commit) — сохранённое состояние проекта с уникальным идентификатором. Каждое сохранение сопровождается осмысленным описанием выполненной работы.

## Ход работы
Для начала я скачала установочный файл Git с официального сайта git-scm.com и запустила установщик, оставив все параметры по умолчанию. После завершения установки я проверила её корректность в терминале, и на экране отобразилась текущая версия программы, что подтвердило успешную установку. Затем я выполнила глобальную настройку Git, указав своё имя и адрес электронной почты; для email использовала тот же адрес, на который зарегистрирован аккаунт на GitHub.

```
$ git --version
git version 2.50.1.windows.1

$ git config --global user.name "Полина Зайцева"
$ git config --global user.email "ppolina054@gmail.com"
```

Далее я создала корневую папку prolabs, перешла в неё через терминал и инициализировала Git-репозиторий, после чего внутри папки появилась скрытая директория .git.

```
$ mkdir prolabs
$ cd prolabs
$ git init
Initialized empty Git repository in C:/Users/Student/prolabs/.git/
```
Внутри корневой папки я создала каталог первой лабораторной работы llb1 и рабочий файл main.lb1.py. Проверив состояние репозитория, я увидела, что папка llb1 подсвечена красным как неотслеживаемая, после чего подготовила файлы к сохранению и сделала первый коммит с описанием «Initial commit: create structure and llb1».

```
$ git status
On branch master
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        llb1/
nothing added to commit but untracked files present (use "git add" to track)

$ git add .
$ git commit -m "Initial commit: create structure and llb1"
[master (root-commit) 068f5d0] Initial commit: create structure and llb1
 1 file changed, 1 insertion(+)
 create mode 100644 llb1/main.lb1.py
```

Затем я зашла на сайт github.com, вошла в свой аккаунт и через иконку «+» создала новый репозиторий с именем prolabs, выбрав тип Public и оставив пустыми все галочки инициализации, так как локальный код уже существовал. После создания репозитория GitHub показал страницу с подсказками, откуда я скопировала и поочерёдно выполнила три команды для связывания локального репозитория с удалённым. При первом выполнении команды отправки система открыла окно браузера для авторизации на GitHub, и я подтвердила доступ. Обновив страницу репозитория в браузере, я убедилась, что структура папки llb1 появилась в удалённом репозитории.

```
$ git remote add origin https://github.com/beeshka158/prolabs.git
$ git branch -M main
$ git push -u origin main

info: please complete authentication in your browser...
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Writing objects: 100% (4/4), 321 bytes | 321.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/beeshka158/prolabs.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```
После оформления отчета в формате Markdown я добавила его в папку llb1 и отправила на GitHub. Проверка состояния репозитория показала, что все изменения успешно синхронизированы с удалённой веткой.

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        llb1/otchet_1.md
nothing added to commit but untracked files present (use "git add" to track)

$ git add .
$ git commit -m "Add report"
[main 1a2b3c4] Add report
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 llb1/otchet_1.md

$ git push
Enumerating objects: 5, done.
...
To https://github.com/beeshka158/prolabs.git
   068f5d0..1a2b3c4  main -> main
```

## Итоги работы
В ходе выполнения лабораторной работы я установила и настроила систему контроля версий Git, создала локальный репозиторий с правильной структурой каталогов для хранения лабораторных работ, выполнила первый коммит с осмысленным описанием, создала публичный удалённый репозиторий на GitHub, связала локальный репозиторий с удалённым и отправила код командой git push, а также освоила оформление отчётов в формате Markdown. Созданная структура папки prolabs позволит в дальнейшем вести все последующие лабораторные работы в едином репозитории: для каждой новой работы достаточно создать новый каталог, сделать коммит и отправить изменения командой git push.
