# 📘 README.md
 
 ** Batch ETL Pipeline for Sales Data**

## 📌 **Project Overview**
This project implements a **batch ETL pipeline** that ingests raw sales data from CSV, transforms it into a clean analytical dataset, and loads it into a **PostgreSQL** database.  
It demonstrates core Data Engineering skills including:

- **Data extraction**  
- **Data cleaning & transformation**  
- **Database loading**  
- **Schema design**  
- **Testing**  
- **Analytics SQL**  

The pipeline is modular, testable, and production‑ready.

---

## 📂 **Project Structure**

```
project-1-batch-etl/
│
├── data/
│   ├── raw/                # Raw input CSV files
│   └── processed/          # Cleaned CSV after transformation
│
├── src/
│   ├── extract.py          # Extract step
│   ├── transform.py        # Transform step (clean_data)
│   └── load.py             # Load step into PostgreSQL
│
├── sql/
│   ├── create_tables.sql   # Table schema
│   └── analytics_queries.sql # BI/analytics SQL queries
│
├── docs/
│   └── architecture.png    # ETL architecture diagram
│
├── tests/
│   └── test_transform.py   # Unit tests for transform logic
│
└── README.md               # Project documentation
```

---

## ⚙️ **Pipeline Architecture**

The ETL pipeline follows a simple left‑to‑right flow:

```
Raw CSV → extract.py → transform.py → load.py → PostgreSQL → Analytics Queries
```

Each step is modular and independently testable.

See the full diagram in:  
`docs/architecture.png`

---

## 🧩 **Components**

### **1. Extract — `extract.py`**
Reads raw CSV files from `data/raw/` and loads them into a pandas DataFrame.  
Handles file validation and logging.

### **2. Transform — `transform.py`**
Contains the core function:

```
clean_data(df)
```

Responsibilities:

- rename columns to snake_case  
- convert numeric fields  
- handle missing values  
- enforce schema consistency  

This logic is fully tested in `tests/test_transform.py`.

### **3. Load — `load.py`**
Loads the cleaned DataFrame into PostgreSQL using SQLAlchemy + pg8000.

Target table:

```
salesdb.public.sales_cleaned
```

Credentials are read from environment variables.

---

## 🧪 **Testing**

Unit tests are implemented using `pytest`.

Test file:

```
tests/test_transform.py
```

The test validates:

- column renaming  
- numeric conversions  
- missing value handling  
- schema consistency  
- exact DataFrame equality  

Run tests from project root:

```
python -m pytest
```

---

## 🗄️ **Database Schema**

Defined in:

```
sql/create_tables.sql
```

Includes:

- table creation  
- column definitions  
- data types  

---

## 📊 **Analytics Queries**

Sample BI queries are stored in:

```
sql/analytics_queries.sql
```

Includes:

- revenue by category  
- profit analysis  
- quantity sold by sub‑category  
- payment mode distribution  

---

## ▶️ **How to Run the Pipeline**

### **1. Run extract**
```
python src/extract.py
```

### **2. Run transform**
```
python src/transform.py
```

### **3. Run load**
```
python src/load.py
```

After loading, data is available in PostgreSQL for analytics.

---

## 🛠️ **Tech Stack**

- Python (pandas, SQLAlchemy, pg8000)  
- PostgreSQL  
- Pytest  
- Logging  
- Modular ETL architecture  

---

## 🚀 **Future Enhancements**

- **Airflow DAG**  
- **Docker Compose for PostgreSQL**  
- **S3 storage + Parquet output**  
- **dbt models**  
- **CI/CD with GitHub Actions**  

---