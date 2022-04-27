<p align="center">
<br><br><br>
<a href="https://github.com/jetfuel-dev/jetfuel"><img src="https://raw.githubusercontent.com/jetfuel-dev/jetfuel/main/assets/jetfuel.png" alt="Jetfuel logo: Jetfuel is the Python Performance Profiler for Production" width="200px"></a>
<br><br>
</p>

<p align="center">
<b>Python Performance Profiling for Production</b><br>
<b>~ It's About Time ~</b>
</p>

Jetfuel is a performance profiler that can monitor the performance of your production Python, and makes results easy to aggregate and search through.

Jetfuel is designed for **Purposeful Profiling**. This means that you only use Jetfuel around code of interest, instead of dumping all code performance logs and mining it later.

Useful for Profiling:

- 🌎 API performance
- 🚀 CI/CD stage / granular performance
- 💡 ML training & inference jobs
- 📀 Database queries
- 📊 Data pipelines / compute jobs

Bad performance has [real world consequences](https://uxplanet.org/how-page-speed-affects-web-user-experience-83b6d6b1d7d7), and is often a result of **lack of visibility**, *even if you are logging it, if it's not be easy to get to, it will be ignored*.

<br>
<p align="center">
<b>What gets measured gets managed!</b>
</p>
<br>

![Continuous Profiling](https://raw.githubusercontent.com/jetfuel-dev/jetfuel/main/assets/continuous_profiling.png)

![Dashboard](https://raw.githubusercontent.com/jetfuel-dev/jetfuel/main/assets/dashboard.png)

<br>

## Installation

```bash
pip install jetfuel-time
```

```bash
docker run -it -p 9000:9000 -v ${PWD}/data:/bin/jetfuel/data jetfuel/jetfuel
```

## Demo

```python
import jetfuel

jetfuel.init(url="http://localhost:9000")

jetfuel.demo()
```

## Usage

```python
# 1. Start / Stop
p = jetfuel.start("Foobar")
pass
p.stop()

# 2. Profiler
with jetfuel.Profiler("Foobar"):
    pass

# 3. Function Decorator
@jetfuel.profiler("Foobar")
def ml_training():
    pass
```
