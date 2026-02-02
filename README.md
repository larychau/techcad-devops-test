```TechCAD DevOps Test Project

DevOps‑пайплайн:  
FastAPI‑сервис → Docker → docker-compose → Prometheus → Grafana → Loki → Promtail → CI/CD.

Описание

Сервис предоставляет эндпоинт `/analyze`, который принимает параметры CAD‑модели и возвращает "оценку технологичности".  
Используется простая dummy ML‑модель (LinearRegression).

Также реализованы:

- контейнеризация (Dockerfile)
- локальный запуск через docker-compose
- метрики Prometheus (`/metrics`)
- визуализация в Grafana
- сбор логов через Loki + Promtail
- CI/CD через GitHub Actions (lint + tests + build)

 Запуск проекта

1. Клонирование репозитория
bash
git clone https://github.com/yourname/techcad-devops-test.git
cd techcad-devops-test

2.Запуск всех сервисов
docker-compose up -d --build

3.Доступ к сервисам
Сервис	URL
FastAPI	http://localhost:8000
Healthcheck	http://localhost:8000/health
Prometheus	http://localhost:9090
Grafana	http://localhost:3000
Loki API	http://localhost:3100

API
POST /analyze
Пример запроса:
{ "complexity": 3.5 } 
Пример ответа:
{ "tech_score": 35.0 } 

Мониторинг
Метрики Prometheus
Доступны по адресу:
http://localhost:8000/metrics 

Grafana
После запуска:
открой http://localhost:3000
логин/пароль по умолчанию: admin / admin
можно импортировать дашборд из grafana/dashboards/techcad-dashboard.json

Логи
Promtail собирает логи контейнеров и отправляет их в Loki.
Пример запроса в Grafana Explore:
{job="docker"} 

CI/CD
Файл workflow:
.github/workflows/ci-cd.yml 
Включает:
black (lint)
flake8 (lint)
pytest (тесты)
сборку Docker образа

Структура проекта
techcad-devops-test/
├── app/                         # Исходный код FastAPI сервиса
│   ├── main.py                  # Основной файл приложения (эндпоинты)
│   ├── model.py                 # Dummy ML-модель (LinearRegression)
│   └── requirements.txt         # Python зависимости
│
├── loki/                        # Конфигурация Loki (хранилище логов)
│   └── local-config.yaml
│
├── prometheus/                  # Конфигурация Prometheus (метрики)
│   └── prometheus.yml
│
├── promtail/                    # Конфигурация Promtail (агент логов)
│   └── config.yml
│
├── .github/
│   └── workflows/               # CI/CD пайплайн GitHub Actions
│       └── ci-cd.yml
│
├── Dockerfile                   # Docker-образ FastAPI приложения
├── docker-compose.yml           # Локальный запуск всех сервисов
├── README.md                    # Документация проекта
