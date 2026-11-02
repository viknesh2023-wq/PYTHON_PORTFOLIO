# CSI3007 — Advanced Python Programming: Lab Submissions Summary (#1 to #7)
**Student:** VIKNESH.G  
**Registration Number:** 23MID0161  
**Course:** Advanced Python Programming (CSI3007)  
**Slot:** L31+L32+L49+L50  
**Faculty:** Dr. Sharmila Banu K  

---

## 📌 Quick Portfolio Integration Guide
Use this document as the master reference to populate your portfolio's digital assignment drawer, modal popups, interactive accordion, or project cards. Each submission is broken down into:
1. **Overview & Objective**: High-level problem statement.
2. **Tasks & Implementations**: What was actually engineered, coded, and analyzed.
3. **Key Concepts & Technical Learnings**: Core Python and algorithmic skills demonstrated.
4. **Ready-to-Paste Card Snippet**: A concise 3-4 bullet point summary ready for your website UI.

---

# Submission #1: Multimodal Ingestion, File Formats & Unicode Encodings
- **Title:** Multimodal Data Pipelines, File Formats (JSON, PDF, Audio) & Character Encoding
- **Date:** 16-07-2026
- **Pages:** 18 Pages

### 1. What Was Done
- **Chinese Character Encoding & Conversion:** Investigated multi-byte character representation using Chinese text (`"你好，世界"`). Programmed bi-directional conversions between `GBK` (Chinese national standard, 2 bytes/char) and `UTF-8` (universal variable encoding, 3 bytes/char) using `.encode()` and `.decode()`. Audited byte-level representations (`b'\xc4\xe3...'` vs `b'\xe4\xbd...'`) to identify encoding mismatches and decode boundaries.
- **PDF Text Ingestion (`pypdf`):** Automated document reading and data harvesting from multi-page research publications (`sample.pdf`). Implemented page counting, extracted raw text across enumerated page streams, and engineered a case-insensitive regex keyword query engine to index research topics.
- **Synthesized Server Log Pipeline:** Constructed a real-time server infrastructure monitoring JSON dataset (`"Server Monitoring Dashboard"`) tracking `system_nodes` (`SRV-001`, `SRV-002`, `SRV-003`), hardware telemetry (`cpu_utilization_pct`, `memory_available_gb`, `active_connections`), and nested alert records.
- **JSON Querying & Validation Engine:** Traversed nested dictionary/list structures, validated syntax integrity, detected null values (`contact_email: null`), and dynamically exported runtime processing analytics to `json_processing_summary.json`.
- **Multimodal Audio Signal Analysis:** Ingested raw audio files using `librosa` and `soundfile`, inspecting sample rates, channel configurations, and waveform metadata.

### 2. What Was Learned
- The fundamental mechanics of Unicode, ANSI, UTF-8, and national character encodings (GBK), and how byte streams behave during serialization.
- Programmatic inspection and text extraction from unstructured PDF documents.
- Nested schema validation, recursive dictionary traversal, and null-safe data querying.
- Multi-format ingestion pipelines combining text, document, structured JSON, and audio streams.

### 3. Ready-to-Paste UI Card Snippet
- **Multimodal Data Pipelines & Encodings:** Handled character conversions (GBK vs UTF-8) and byte stream parsing.
- **Automated PDF Scraping:** Extracted text and indexed multi-page publications using `pypdf`.
- **JSON Telemetry Engine:** Ingested, validated, and queried nested server health logs with automated reporting.
- **Audio Processing:** Processed audio waveforms and extracted metadata using `librosa` & `soundfile`.

---

# Submission #2: High-Performance Numerical Algorithms & LeetCode Problem Solving
- **Title:** Advanced Number Theory & Algorithmic Problem Solving (LeetCode Hard/Medium)
- **Date:** 23-07-2026
- **Pages:** 12 Pages

### 1. What Was Done
- **LeetCode 204 — Count Primes (Optimized Sieve Algorithms):**
  - *Simple Sieve of Eratosthenes:* Generated prime counts up to $N$ by marking multiples of primes up to $\sqrt{N}$, running in $O(N \log \log N)$ time.
  - *Segmented Sieve:* Engineered a memory-efficient segmented sieve to find primes within an arbitrary range `[low, high]` without storing or traversing numbers from $0$ to $\text{low}$, reducing space complexity to $O(\sqrt{\text{high}})$.
- **LeetCode 85 — Maximal Rectangle (Hard):** Formulated an optimal solution to identify the largest rectangle of 1s in a 2D binary matrix. Converted each matrix row into an accumulated 1D histogram height array and evaluated the maximum rectangular area using a monotonic stack in optimal $O(R \times C)$ time.
- **LeetCode 87 — Scramble String (Hard):** Implemented recursive divide-and-conquer string partitioning enhanced with 3D memoization / Dynamic Programming to test scramble equivalency while pruning non-anagram substrings.
- **LeetCode 121 & 123 — Stock Trading Optimization:** Evaluated single-pass greedy minimum tracking for single transactions ($O(N)$) and multi-state dynamic programming for multi-transaction bounds.

### 2. What Was Learned
- Algorithmic space-time optimization techniques, replacing brute-force traversals with mathematical sieves.
- Monotonic stack data structures for solving 2D geometric and histogram optimization problems in linear time.
- State-space memoization and dynamic programming branch pruning.
- Mathematical complexity trade-offs between global sieving and localized segmented windowing.

### 3. Ready-to-Paste UI Card Snippet
- **Optimized Prime Sieves:** Implemented Simple and Segmented Sieves of Eratosthenes for large numerical windows.
- **Maximal Rectangle (LeetCode 85):** Monotonic stack and 2D histogram dimension reduction in $O(R \times C)$ time.
- **Scramble String & DP:** Solved complex recursive string partitioning with memoized Dynamic Programming.
- **Stock Market Algorithms:** Single and multi-transaction profit optimization with state-space tracking.

---

# Submission #3: UI/UX System Architecture & Executive Dashboard — "Script Analyzer"
- **Title:** Enterprise Product Architecture & Executive Production Dashboard
- **Team:** Ramanand S P, Monish Jagatheswaran, Narmatha N, Karishma A, Viknesh G (23MID0161)
- **Course & Slot:** CSI3007 (L31+L32+L49+L50) | Faculty: Dr. Sharmila Banu K
- **Date:** 30-07-2026
- **Pages:** 2 Pages

### 1. What Was Done
- **Script Analyzer & Production Estimator:** Collaborated on a full-stack media production analytics application designed to analyze movie scripts, predict budgetary constraints, and calculate logistical schedules.
- **Viknesh's Individual Contribution — Executive Dashboard Architecture:**
  - *Executive KPI Bar:* Designed metric widgets tracking Budget (\$9.8M vs \$9.57M estimate), Runtime (1h 52m on target), Shoot Duration (48 shoot days vs 50 planned), Projected ROI ($3.2\times$), Risk Index (Medium — 3 high-risk sequences), and Project Health Score (87/100).
  - *Budget Tracking Spline:* Visualized multi-phase production expenditures (Pre-Prod, Weeks 1-4, Post, VFX) comparing Allocated vs Actual spend.
  - *Cost Breakdown Donut Chart:* Modeled departmental allocation across Cast & Crew (38%), Locations (22%), Equipment (18%), Post & VFX (14%), and Other (8%).
  - *AI Recommendations Panel:* Designed predictive machine-learning suggestion cards highlighting actionable optimizations (e.g., merging desert shoot schedules to save \$180K in logistics).
  - *Live Audit Trail:* Integrated a streaming recent activity feed logging script revisions (`v2.3`), scout reports, and approvals.

### 2. What Was Learned
- High-level system architecture and executive data visualization for financial/logistical pipelines.
- Modern dashboard UI/UX patterns (KPI summaries, spline charts, multi-segment donut distributions).
- Structuring actionable AI recommendations within enterprise business intelligence interfaces.
- Translating complex raw dataset schemas into human-readable, executive-level telemetry.

### 3. Ready-to-Paste UI Card Snippet
- **Executive Production Dashboard:** Complete architecture and UI design for film budget/schedule analytics.
- **Real-Time KPI & Financial Telemetry:** Modeled budget burn rates, projected ROI, and phase-wise cost distributions.
- **AI Recommendation Engine:** Designed interactive suggestion cards optimizing high-cost operational decisions.
- **Live Activity Feed:** Implemented real-time audit logs tracking script iterations and logistical sign-offs.

---

# Submission #4: OOP Architecture, Multithreading & Concurrency Synchronization
- **Title:** Object-Oriented Domain Modeling & Multithreaded Concurrency Synchronization
- **Date:** 07-08-2026 & 27-08-2026
- **Pages:** 23 Pages

### 1. What Was Done
- **Task 1 — `Student` Class (Academic Tracker):** Encapsulated student academic data with constructor `__init__(self, name, student_id)`, dynamic test score ingestion `add_score()`, statistical calculation `calculate_average()`, and automated grading logic `get_final_grade()` (60% pass threshold), complete with input validation and missing score handling.
- **Task 2 — `Gene` Class (Bioinformatics DNA Handler):** Modeled genomic DNA strands with strict validation assertions rejecting RNA uracil (`assert 'U' not in new_sequence.upper()`). Implemented nucleotide frequency counter `base_composition()` and GC-content ratio evaluator `gc_content()` ($(\text{G} + \text{C}) / \text{Length}$).
- **Task 3 — Multithreading Priority Queue & Synchronization:** Built a multithreaded worker dispatching system and developed an original **"Hospital Triage Analogy"**:
  - Triage nurses modeled as worker threads (`Thread-1`, `Thread-2`, `Thread-3`).
  - Arriving patients modeled as prioritized tasks (Low, Medium, High urgency).
  - Mutex thread locking (`queueLock.acquire()`, `queueLock.release()`) preventing race conditions during patient retrieval.
  - Graceful thread termination via global flags (`thread_exit_Flag = 1`) and thread joining (`thread.join()`).
- **Task 4 — Concurrency Benchmarking:** Benchmarked execution throughput between manual `threading.Thread` workers and `concurrent.futures.ThreadPoolExecutor` using high-resolution timers (`time.perf_counter()`), proving thread pooling minimizes creation overhead and optimizes execution time.

### 2. What Was Learned
- Object-oriented programming principles (encapsulation, validation guards, instance methods).
- Concurrency pitfalls: race conditions, deadlock prevention, and thread synchronization using mutex locks.
- Thread-safe priority queue processing (Producer-Consumer architecture).
- High-level concurrent worker pool scaling (`ThreadPoolExecutor`) vs low-level thread lifecycle control.

### 3. Ready-to-Paste UI Card Snippet
- **OOP Domain Modeling:** Built robust encapsulated models for Student performance tracking and DNA bioinformatics.
- **Hospital Triage Concurrency Analogy:** Designed a synchronized multi-worker system utilizing mutex queue locks.
- **Race Condition Prevention:** Synchronized shared data access with acquire/release locking mechanisms.
- **ThreadPoolExecutor Benchmarking:** Profiled and accelerated multi-worker execution over sequential processing.

---

# Submission #5: High-Efficiency Data Ingestion: `csv` Module vs `pandas`
- **Title:** High-Efficiency Data Serialization & Ingestion: Python `csv` vs `pandas`
- **Date:** 03-09-2026
- **Pages:** 6 Pages

### 1. What Was Done
- **Part 1 — Low-Level Stream I/O with Python `csv`:** Created and managed `students.csv` with schema `['Student Name', 'CGPA', 'Certifications_Count', 'Internship_Exp_yrs']`. Evaluated sequential row streaming (`writer.writerow()`) vs batch matrix ingestion (`writer.writerows()`), reading and printing streams with `csv.reader()`.
- **Part 2 — Tabular Data Processing with `pandas`:** Loaded data into memory with `pd.read_csv()`, manipulated schema attributes, and serialized structured frames back to disk with `df.to_csv(index=False)`.
- **Part 3 — Dynamic DataFrame Concatenation:** Merged new candidate records using `pd.concat([df_read, new_rows], ignore_index=True)`. Handled index realignment, missing value propagation (`NaN`), and column datatype inference.
- **Part 4 — Dictionary & JSON Ingestion:** Loaded nested Python dictionary collections into tabular DataFrames, validating schema compatibility and automated column assignment.

### 2. What Was Learned
- The fundamental performance trade-offs between streaming disk I/O (`csv`) and vectorized in-memory tabular structures (`pandas`).
- File stream pointer operations, newline handling, and memory footprint management.
- Dynamic schema evolution, index alignment, and `NaN` handling during dataframe concatenation.

### 3. Ready-to-Paste UI Card Snippet
- **Low-Level Stream I/O:** Streamed and parsed tabular CSV data using Python's native `csv` module.
- **Pandas Ingestion Pipeline:** Implemented end-to-end reading, transformation, and sanitized CSV exports.
- **Data Concatenation & NaN Handling:** Managed index realignment and missing value propagation with `pd.concat()`.
- **Dictionary/JSON Parsing:** Converted nested Python dictionary structures into structured 2D DataFrames.

---

# Submission #6: Pandas Series & Hierarchical Indexing Deep Dive
- **Title:** Advanced Pandas Series Architecture & Multi-Level Hierarchical Indexing
- **Date:** September 2026
- **Pages:** 15 Pages

### 1. What Was Done
- **Part 1 — Series Construction & Custom Indexing:** Constructed 1D labeled series from Python lists, tuples, and dictionaries. Configured custom indices mapping student names to degree programs (`B.Sc CS`, `B.Com`, `BBA`, `B.Sc Maths`, `BCA`). Set series metadata attributes (`name='Programme'`, `index.name='Student_Name'`).
- **Part 2 — Missing Data & Type Auditing:** Evaluated explicit `None` and `np.nan` values, analyzed automatic datatype casting behavior (`object` vs float/int), and applied boolean filters.
- **Part 3 — Retail Inventory Analytics:** Modeled product inventory (Names, Prices, Quantities) to compute descriptive statistics: maximum stock volume, highest-priced asset, and total valuation.
- **Part 4 — Hierarchical Multi-Index Architecture (`pd.MultiIndex`):** Engineered a multi-level series modeling student marks across two distinct tiers: Semesters (`Sem1`, `Sem2`) and Course Subjects (`Maths`, `Physics`, `Chemistry`).
- **Part 5 — MultiIndex Accessors & Slicing:** Implemented multi-dimensional querying using tuple label slicing (`.loc[(semester, subject)]`) and positional integer offsets (`.iloc[]`).

### 2. What Was Learned
- Internal architecture and memory model of Pandas Series compared to native Python sequences.
- Type casting rules and numerical stability when handling missing values (`NaN`).
- Constructing and traversing multi-dimensional hierarchical indices (`MultiIndex`).
- Coordinate-based tuple lookups (`.loc`) vs positional indexing (`.iloc`).

### 3. Ready-to-Paste UI Card Snippet
- **1D Labeled Series:** Mastered custom-indexed series construction from lists, tuples, and dictionaries.
- **Missing Value Handling:** Audited `NaN` propagation, automatic dtype casting, and boolean filtering masks.
- **Retail Data Modeling:** Evaluated extreme metrics (costliest item, peak stock) using vectorized operations.
- **Hierarchical MultiIndex:** Designed multi-tier semester/subject index structures with coordinate tuple slicing.

---

# Submission #7: DataFrame Operations & Global Green View Index (GVI) Analysis
- **Title:** Global Urban Environmental Analytics: Green View Index (GVI) DataFrame Study
- **Date:** 24-04-2026
- **Pages:** 7 Pages

### 1. What Was Done
- **Urban Canopy Dataset Architecture:** Structured a real-world environmental dataset of 30 major global cities with attributes: `RANK`, `CITY`, `COUNTRY`, and `GVI` (Green View Index — percentage of canopy visibility at street level). Dataset included Tampa (36.1), Singapore (29.3), Oslo (28.8), Vancouver (25.9), Amsterdam (20.6), and Paris (8.8).
- **Vectorized Boolean Filtering:** Extracted national urban subsets using Boolean masks (`df[df['COUNTRY'] == target]`).
- **Statistical & Aggregational Analysis:**
  - Evaluated national mean GVI for the USA using `.mean()` (`21.4125`).
  - Computed minimum urban green cover in the Netherlands using `.min()` and `df.groupby()`.
  - Computed total cumulative GVI sum across Italian metropolitan centers using `df.loc[..., 'GVI'].sum()` (`16.2`).
- **Comparative Querying & Pivot Reshaping:** Benchmarked three indexing strategies (boolean masks, `.loc` label access, `.iloc` coordinate lookups), structured multidimensional pivot tables, and sorted global green index leaders using `df.sort_values(by="GVI", ascending=False)`.

### 2. What Was Learned
- Exploratory Data Analysis (EDA) workflows on urban environmental metrics.
- Vectorized query efficiency: comparing boolean masking, `.loc`, and `.iloc`.
- GroupBy statistical aggregations, multi-level summarization, and pivot tables.
- Sorting, filtering, and rank analysis on large tabular datasets.

### 3. Ready-to-Paste UI Card Snippet
- **Global Urban Canopy Analytics:** Structured and analyzed Green View Index (GVI) metrics across 30 world cities.
- **Vectorized Query Optimization:** Benchmarked Boolean filtering, `.loc` label access, and `.iloc` coordinate slicing.
- **National Statistical Aggregation:** Evaluated national GVI means, minimums, and cumulative sums using `groupby()`.
- **Pivot Table Reshaping:** Synthesized multidimensional pivot tables and ranked global urban canopy leaders.

---

