import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

# ─────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Taller #1 – Estadística 3",
    page_icon="📊",
    layout="wide",
)

# ─────────────────────────────────────────────
# ESTILOS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }

    .header-banner {
        background: linear-gradient(135deg, #0d1b2a 0%, #1b3a5c 60%, #0d2b45 100%);
        border-left: 6px solid #f0a500;
        border-radius: 10px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        color: #e8f4fd;
    }
    .header-banner h1 {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 2.1rem;
        color: #f0a500;
        margin: 0 0 0.5rem 0;
        letter-spacing: -1px;
    }
    .header-banner .meta { font-size: 0.95rem; color: #9ecae8; margin: 2px 0; }
    .header-banner .name-field {
        display: inline-block;
        border-bottom: 2px dashed #f0a500;
        color: #ffffff;
        font-weight: 700;
        min-width: 220px;
        padding: 0 4px;
    }
    .part-badge {
        display: inline-block;
        background: #f0a500;
        color: #0d1b2a;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.85rem;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 20px;
        margin-right: 8px;
        letter-spacing: 0.5px;
    }
    .part-header {
        background: linear-gradient(90deg, #0d1b2a 0%, #1b3a5c 100%);
        border-left: 6px solid #f0a500;
        border-radius: 8px;
        padding: 1.2rem 1.8rem;
        margin: 2.5rem 0 1.5rem 0;
        color: #e8f4fd;
    }
    .part-header h2 {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.4rem;
        color: #f0a500;
        margin: 0 0 0.3rem 0;
    }
    .part-header p { font-size: 0.9rem; color: #9ecae8; margin: 0; }
    .section-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.15rem;
        color: #1b3a5c;
        font-weight: 600;
        border-bottom: 2px solid #f0a500;
        padding-bottom: 6px;
        margin-bottom: 1rem;
        margin-top: 1rem;
    }
    .explain-box {
        background: #fffbf0;
        border-left: 4px solid #f0a500;
        border-radius: 6px;
        padding: 0.9rem 1.2rem;
        font-size: 0.9rem;
        color: #3d3d3d;
        margin-top: 0.8rem;
        margin-bottom: 1rem;
    }
    .stat-card {
        background: linear-gradient(135deg, #0d1b2a 0%, #1b3a5c 100%);
        border-radius: 10px;
        padding: 1rem 1.2rem;
        color: #e8f4fd;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .stat-card .label {
        font-size: 0.78rem;
        color: #9ecae8;
        font-family: 'IBM Plex Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .stat-card .value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #f0a500;
        font-family: 'IBM Plex Mono', monospace;
    }
    .stat-card .sub { font-size: 0.72rem; color: #88bbd8; margin-top: 2px; }
    .alert-box-red {
        background: #fde8e8;
        border-left: 4px solid #e63946;
        border-radius: 6px;
        padding: 0.7rem 1.1rem;
        font-size: 0.88rem;
        color: #7a1a1a;
        margin: 0.6rem 0;
    }
    .alert-box-green {
        background: #e8f8ee;
        border-left: 4px solid #2a9d5c;
        border-radius: 6px;
        padding: 0.7rem 1.1rem;
        font-size: 0.88rem;
        color: #1a5c34;
        margin: 0.6rem 0;
    }
    .lib-pill {
        display: inline-block;
        background: #1b3a5c;
        color: #f0a500;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.78rem;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 2px 3px;
    }
    .divider-var {
        border: none;
        border-top: 3px dashed #c0d8f0;
        margin: 2.5rem 0 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER PRINCIPAL
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-banner">
    <h1>📊 Taller #1 &mdash; Estadística 3</h1>
    <p class="meta">Carrera: &nbsp;<strong>Ingeniería de Sistemas</strong></p>
    <p class="meta">Estudiante: &nbsp;<span class="name-field">Andres Felipe Velez Alcaraz</span></p>
    <p class="meta">Profesor: &nbsp;<span class="name-field">Daniel Betancur Trujillo</span></p>
    <p class="meta" style="margin-top:0.9rem;">
        <span class="part-badge">Parte 1</span>
        Tablas de Frecuencia · Gráficas de Pareto · Gráfica Radar (Municipio × EPS)
    </p>
    <p class="meta" style="margin-top:0.4rem;">
        <span class="part-badge">Parte 2</span>
        Variables Cuantitativas · Cuartiles · Boxplot · Dispersión · Histograma
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LIBRERÍAS (unificadas)
# ─────────────────────────────────────────────
with st.expander("📦 Librerías utilizadas en este taller", expanded=False):
    st.markdown("""
    <div style="padding:0.5rem 0">
    <span class="lib-pill">pandas</span>
    <span class="lib-pill">matplotlib</span>
    <span class="lib-pill">numpy</span>
    <span class="lib-pill">scipy</span>
    <span class="lib-pill">streamlit</span>
    </div>

    | Librería | Descripción |
    |---|---|
    | **pandas** | Manipulación y análisis de datos tabulares. `pd.crosstab()` para tablas cruzadas, `pd.cut()` para intervalos de frecuencia, `quantile()` para cuartiles. |
    | **matplotlib** | Visualización 2D: diagramas de Pareto, gráfica radar, boxplot, dispersión e histograma. |
    | **numpy** | Cálculos vectoriales: ángulos de la gráfica radar con `np.linspace`, eje X para dispersión. |
    | **scipy** | `stats.skew()` y `stats.kurtosis()` para asimetría y curtosis exactas. `gaussian_kde` para curva de densidad. |
    | **streamlit** | Framework que convierte el script Python en una aplicación web interactiva sin HTML/CSS/JS adicional. |
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PALETA GLOBAL
# ─────────────────────────────────────────────
AZUL        = '#1b3a5c'
DORADO      = '#f0a500'
ROJO        = '#e63946'
VERDE       = '#2a9d5c'
ROJO_PARETO = '#e63946'
PALETA      = ['#1b3a5c','#f0a500','#4a7fa5','#e8a020',
               '#88bbd8','#f7c948','#c9e2f0','#0d2b45',
               '#2e86ab','#a23b72','#f18f01','#c73e1d']

COLORES_VAR = {
    "Logica_y_Programacion":        '#1b3a5c',
    "Estructuras_de_Datos":         '#f0a500',
    "Machine_Learning":             '#2e86ab',
    "Calculo_Diferencial":          '#a23b72',
    "Arquitectura_de_Computadores": '#f18f01',
}


# ══════════════════════════════════════════════════════════
# ██████████████████  PARTE 1  ██████████████████████████████
# ══════════════════════════════════════════════════════════
st.markdown("""
<div class="part-header">
    <h2>📂 Parte 1 — Variables Cualitativas</h2>
    <p>Tablas de Frecuencia · Diagramas de Pareto · Gráfica Radar Cruzada (Municipio × EPS)</p>
</div>
""", unsafe_allow_html=True)

# ── Carga CSV Parte 1 ─────────────────────────────────────
st.markdown('<div class="section-title">📂 Datos cargados — 04 - estudiantes.csv</div>',
            unsafe_allow_html=True)

df = pd.read_csv("04 - estudiantes.csv")
st.dataframe(df, use_container_width=True)
st.caption(f"Total registros: {len(df)} estudiantes · {len(df.columns)} variables")

# ── Helpers Parte 1 ───────────────────────────────────────
def tabla_frecuencia(serie: pd.Series, nombre_col: str) -> pd.DataFrame:
    tabla = pd.DataFrame()
    tabla['F. Absoluta']       = serie.value_counts().sort_index()
    tabla['F. Relativa (%)']   = serie.value_counts(normalize=True).sort_index() * 100
    tabla['F. Acumulada']      = tabla['F. Absoluta'].cumsum()
    tabla['F. Rel. Acum. (%)'] = tabla['F. Relativa (%)'].cumsum()
    tabla.reset_index(inplace=True)
    tabla.rename(columns={'index': nombre_col}, inplace=True)
    tabla['F. Relativa (%)']   = tabla['F. Relativa (%)'].round(2)
    tabla['F. Rel. Acum. (%)'] = tabla['F. Rel. Acum. (%)'].round(2)
    return tabla

def grafica_pareto(pareto_df, col_cat, titulo, ancho=10):
    n       = len(pareto_df)
    colores = [PALETA[i % len(PALETA)] for i in range(n)]
    fig, ax1 = plt.subplots(figsize=(ancho, 5))
    bars = ax1.bar(pareto_df[col_cat], pareto_df['F. Absoluta'],
                   color=colores, edgecolor='white', linewidth=1.2, zorder=3)
    ax1.set_ylabel('Frecuencia Absoluta', color=AZUL, fontsize=11, fontweight='bold')
    ax1.set_xlabel(col_cat, fontsize=11)
    ax1.set_ylim(0, pareto_df['F. Absoluta'].max() * 1.45)
    ax1.yaxis.grid(True, linestyle='--', alpha=0.45, zorder=0)
    ax1.set_facecolor('#f7fafd')
    fig.patch.set_facecolor('#f7fafd')
    plt.xticks(rotation=30, ha='right', fontsize=9)
    for bar in bars:
        ax1.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + pareto_df['F. Absoluta'].max() * 0.02,
                 str(int(bar.get_height())),
                 ha='center', va='bottom', fontsize=11, fontweight='bold', color=AZUL)
    ax2 = ax1.twinx()
    ax2.plot(pareto_df[col_cat], pareto_df['F. Rel. Acum. (%)'],
             color=ROJO_PARETO, marker='o', linewidth=2.5, markersize=8, zorder=4)
    ax2.axhline(80, color=ROJO_PARETO, linestyle='--', linewidth=1.2, alpha=0.6)
    ax2.set_ylabel('F. Relativa Acumulada (%)', color=ROJO_PARETO, fontsize=11, fontweight='bold')
    ax2.set_ylim(0, 120)
    ax2.tick_params(axis='y', labelcolor=ROJO_PARETO)
    ax1.set_title(titulo, fontsize=13, fontweight='bold', color=AZUL, pad=12)
    ph1 = mpatches.Patch(color=AZUL,        label='F. Absoluta (barras)')
    ph2 = mpatches.Patch(color=ROJO_PARETO, label='F. Rel. Acumulada (línea)')
    ax1.legend(handles=[ph1, ph2], loc='upper left', fontsize=9)
    plt.tight_layout()
    return fig


# ══════════════════════════════════════════════
#  P1 — SECCIÓN 1: PARETO MUNICIPIO
# ══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🏙️ Sección 1 — Pareto: Municipio de Residencia</div>',
            unsafe_allow_html=True)
st.markdown("""
<div class="explain-box">
ℹ️ <strong>¿Qué es la gráfica de Pareto?</strong><br>
Combina barras ordenadas de mayor a menor (frecuencia absoluta) con una línea de frecuencia
relativa acumulada. Permite identificar las categorías que concentran la mayor parte de los datos.
La línea punteada roja en el 80 % ilustra el principio de Pareto.<br><br>
En este caso muestra <strong>en qué municipios viven más estudiantes</strong>, ordenados de mayor a menor.
</div>
""", unsafe_allow_html=True)

tabla_mun  = tabla_frecuencia(df['Municipio_Residencia'], 'Municipio_Residencia')
pareto_mun = tabla_mun.sort_values('F. Absoluta', ascending=False).reset_index(drop=True)

col1, col2 = st.columns([1.1, 1.9])
with col1:
    st.markdown("**Tabla de frecuencia — Municipio**")
    st.dataframe(tabla_mun, use_container_width=True, hide_index=True)
with col2:
    st.markdown("**Interpretación**")
    for _, row in pareto_mun.iterrows():
        st.markdown(f"- **{row['Municipio_Residencia']}**: "
                    f"{int(row['F. Absoluta'])} estudiante(s) "
                    f"({row['F. Relativa (%)']:.1f} %)")

fig_mun = grafica_pareto(pareto_mun, 'Municipio_Residencia',
                          'Diagrama de Pareto — Municipio de Residencia', ancho=11)
st.pyplot(fig_mun)


# ══════════════════════════════════════════════
#  P1 — SECCIÓN 2: PARETO EPS
# ══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🏥 Sección 2 — Pareto: EPS</div>',
            unsafe_allow_html=True)
st.markdown("""
<div class="explain-box">
ℹ️ La gráfica de Pareto para <strong>EPS</strong> muestra qué entidades de salud concentran
la mayor cantidad de estudiantes, ordenadas de mayor a menor. Permite identificar cuáles EPS
tienen más afiliados dentro del grupo y cuáles tienen poca representación.
</div>
""", unsafe_allow_html=True)

tabla_eps  = tabla_frecuencia(df['EPS'], 'EPS')
pareto_eps = tabla_eps.sort_values('F. Absoluta', ascending=False).reset_index(drop=True)

col3, col4 = st.columns([1, 2])
with col3:
    st.markdown("**Tabla de frecuencia — EPS**")
    st.dataframe(tabla_eps, use_container_width=True, hide_index=True)
with col4:
    st.markdown("**Interpretación**")
    for _, row in pareto_eps.iterrows():
        st.markdown(f"- **{row['EPS']}**: "
                    f"{int(row['F. Absoluta'])} estudiante(s) "
                    f"({row['F. Relativa (%)']:.1f} %)")

fig_eps = grafica_pareto(pareto_eps, 'EPS', 'Diagrama de Pareto — EPS', ancho=9)
st.pyplot(fig_eps)


# ══════════════════════════════════════════════
#  P1 — SECCIÓN 3: TABLA CRUZADA
# ══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🔀 Sección 3 — Tabla Cruzada: Municipio × EPS</div>',
            unsafe_allow_html=True)
st.markdown("""
<div class="explain-box">
ℹ️ <strong>¿Qué es una tabla cruzada?</strong><br>
Es una tabla de doble entrada que cruza dos variables categóricas usando <code>pd.crosstab()</code>.
Las <strong>filas</strong> son los municipios, las <strong>columnas</strong> las EPS, y cada celda
indica cuántos estudiantes de ese municipio están afiliados a esa EPS.
La columna <strong>TOTAL</strong> suma todos los estudiantes por municipio y la fila
<strong>TOTAL</strong> suma todos por EPS.
Esta tabla alimenta directamente la gráfica radar de la siguiente sección.
</div>
""", unsafe_allow_html=True)

tabla_cruzada = pd.crosstab(
    df['Municipio_Residencia'], df['EPS'],
    margins=True, margins_name='TOTAL'
)
tabla_cruzada.index.name = 'Municipio \\ EPS'
st.dataframe(tabla_cruzada, use_container_width=True)

st.markdown("""
<div class="explain-box">
📌 <strong>Ejemplo de lectura:</strong> busca la fila de un municipio y recorre sus columnas
para ver cuántos estudiantes de allí están en cada EPS.
La fila <em>TOTAL</em> indica cuántos estudiantes hay por EPS en todo el grupo.
La columna <em>TOTAL</em> indica cuántos estudiantes hay por municipio en total.
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  P1 — SECCIÓN 4: GRÁFICA RADAR
# ══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🕸️ Sección 4 — Gráfica Radar: Municipio × EPS</div>',
            unsafe_allow_html=True)
st.markdown("""
<div class="explain-box">
ℹ️ <strong>¿Qué muestra esta gráfica radar?</strong><br>
Cada <strong>eje</strong> corresponde a un municipio de residencia. La distancia desde el centro
indica cuántos estudiantes de ese municipio pertenecen a una EPS (valores absolutos reales).<br><br>
Cada <strong>polígono coloreado</strong> representa una EPS distinta. Polígono grande y uniforme →
afiliados repartidos equitativamente. Picos en ciertos ejes → concentración en esos municipios.
</div>
""", unsafe_allow_html=True)

radar_df   = tabla_cruzada.drop(index='TOTAL')
eps_lista  = [c for c in radar_df.columns if c != 'TOTAL']
municipios = list(radar_df.index)
N          = len(municipios)
angles     = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles    += angles[:1]
MAX_ESCALA = int(radar_df[eps_lista].values.max())

fig_radar, ax_r = plt.subplots(figsize=(11, 10), subplot_kw=dict(polar=True))
ax_r.set_facecolor('#f0f6fc')
fig_radar.patch.set_facecolor('#f7fafd')

for i, eps in enumerate(eps_lista):
    vals  = [int(radar_df.loc[m, eps]) for m in municipios]
    vals += vals[:1]
    color = PALETA[i % len(PALETA)]
    ax_r.plot(angles, vals, color=color, linewidth=2.2, label=eps)
    ax_r.fill(angles, vals, color=color, alpha=0.10)
    for ang, val in zip(angles[:-1], vals[:-1]):
        if val > 0:
            ax_r.annotate(str(val), xy=(ang, val),
                          xytext=(ang, val + MAX_ESCALA * 0.04),
                          fontsize=6.5, color=color, fontweight='bold',
                          ha='center', va='bottom')

ax_r.set_xticks(angles[:-1])
ax_r.set_xticklabels(municipios, fontsize=9, color=AZUL, fontweight='bold')
paso       = 20
ticks_vals = list(range(0, MAX_ESCALA + paso, paso))
ax_r.set_ylim(0, MAX_ESCALA + 10)
ax_r.set_yticks(ticks_vals)
ax_r.set_yticklabels([str(v) for v in ticks_vals], fontsize=7, color='gray')
ax_r.set_title(
    f'Gráfica Radar — Estudiantes por EPS en cada Municipio\n'
    f'(ejes = municipios · cada polígono = una EPS · escala: 0 – {MAX_ESCALA} estudiantes)',
    fontsize=11, fontweight='bold', color=AZUL, pad=32)
ax_r.legend(loc='upper right', bbox_to_anchor=(1.6, 1.2),
            fontsize=9, title='EPS', title_fontsize=10)
ax_r.grid(color='#c0d8f0', linestyle='--', linewidth=0.8)
plt.tight_layout()
st.pyplot(fig_radar)

st.markdown(f"""
<div class="explain-box">
📌 <strong>Cómo leer la gráfica paso a paso:</strong><br>
1. Elige una <strong>EPS</strong> en la leyenda e identifica su color.<br>
2. Observa qué ejes (municipios) alcanza más lejos desde el centro.<br>
3. El número en cada vértice es la cantidad exacta de estudiantes de ese municipio en esa EPS.<br>
4. Compara polígonos: uno que envuelve a otro tiene más afiliados en esos municipios.<br><br>
<strong>Escala fija 0 – {MAX_ESCALA}:</strong> permite comparar directamente todas las EPS y municipios
sin distorsión por normalización.
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
# ██████████████████  PARTE 2  ██████████████████████████████
# ══════════════════════════════════════════════════════════
st.markdown("""
<div class="part-header">
    <h2>📈 Parte 2 — Variables Cuantitativas</h2>
    <p>Tabla de Frecuencia por Intervalos · Cuartiles (Tukey) · Boxplot · Dispersión · Histograma KDE</p>
</div>
""", unsafe_allow_html=True)

# ── Carga CSV Parte 2 ─────────────────────────────────────
st.markdown('<div class="section-title">📂 Datos cargados — 05 - notas1.csv</div>',
            unsafe_allow_html=True)

data = pd.read_csv("05 - notas1.csv")
st.dataframe(data, use_container_width=True)
st.caption(f"Total registros: {len(data)} estudiantes · {len(data.columns)} variables")

# ── Variables analizadas ──────────────────────────────────
VARIABLES = [
    "Logica_y_Programacion",
    "Estructuras_de_Datos",
    "Machine_Learning",
    "Calculo_Diferencial",
    "Arquitectura_de_Computadores",
]
NOMBRES_DISPLAY = {
    "Logica_y_Programacion":        "Lógica y Programación",
    "Estructuras_de_Datos":         "Estructuras de Datos",
    "Machine_Learning":             "Machine Learning",
    "Calculo_Diferencial":          "Cálculo Diferencial",
    "Arquitectura_de_Computadores": "Arquitectura de Computadores",
}
EMOJIS = {
    "Logica_y_Programacion":        "💻",
    "Estructuras_de_Datos":         "🌲",
    "Machine_Learning":             "🤖",
    "Calculo_Diferencial":          "∫",
    "Arquitectura_de_Computadores": "🖥️",
}

# ── Helpers Parte 2 ───────────────────────────────────────
def tabla_frecuencia_continua(serie: pd.Series, bins: int = 6) -> pd.DataFrame:
    cortado = pd.cut(serie, bins=bins)
    tabla = pd.DataFrame()
    tabla['Intervalo']         = cortado.value_counts().sort_index().index.astype(str)
    tabla['F. Absoluta']       = cortado.value_counts().sort_index().values
    tabla['F. Relativa (%)']   = (cortado.value_counts(normalize=True).sort_index().values * 100).round(2)
    tabla['F. Acumulada']      = tabla['F. Absoluta'].cumsum()
    tabla['F. Rel. Acum. (%)'] = tabla['F. Relativa (%)'].cumsum().round(2)
    return tabla

def analisis_tukey(serie: pd.Series):
    Q1  = serie.quantile(0.25)
    Q2  = serie.quantile(0.50)
    Q3  = serie.quantile(0.75)
    fs  = Q3 - Q1
    lim_inf = Q1 - 1.5 * fs
    lim_sup = Q3 + 1.5 * fs
    return Q1, Q2, Q3, fs, lim_inf, lim_sup, serie[serie < lim_inf], serie[serie > lim_sup]

def tipo_curtosis(k):
    if k > 0:  return "Leptocúrtica 🔺 (pico pronunciado, colas pesadas)"
    elif k < 0: return "Platicúrtica 🔻 (distribución aplanada, colas ligeras)"
    else:       return "Mesocúrtica ➖ (similar a la distribución normal)"

def tipo_asimetria(s):
    if s > 0.1:   return "Asimetría positiva → cola derecha larga (sesgo derecho)"
    elif s < -0.1: return "Asimetría negativa → cola izquierda larga (sesgo izquierdo)"
    else:          return "Distribución aproximadamente simétrica"

def graficar_trio(serie, nombre, color, Q1, Q2, Q3, lim_inf, lim_sup, atip_izq, atip_der):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.patch.set_facecolor('#f7fafd')
    for ax in axes:
        ax.set_facecolor('#f0f6fc')

    # ── Boxplot ──
    ax1 = axes[0]
    ax1.boxplot(serie.dropna(), vert=True, patch_artist=True, widths=0.5,
                medianprops=dict(color=DORADO, linewidth=3),
                boxprops=dict(facecolor=color, alpha=0.4, linewidth=1.5),
                whiskerprops=dict(color=color, linewidth=1.8, linestyle='--'),
                capprops=dict(color=color, linewidth=2.5),
                flierprops=dict(marker='o', color=ROJO, markersize=7,
                                markerfacecolor=ROJO, alpha=0.8))
    ax1.axhline(Q1, color='#4a7fa5', linestyle=':', linewidth=1.4, label=f'Q1 = {Q1:.2f}')
    ax1.axhline(Q2, color=DORADO,   linestyle='-',  linewidth=2,   label=f'Q2 = {Q2:.2f}')
    ax1.axhline(Q3, color='#2e86ab', linestyle=':', linewidth=1.4, label=f'Q3 = {Q3:.2f}')
    ax1.axhline(lim_inf, color=ROJO, linestyle='--', linewidth=1,  label=f'Lím.inf = {lim_inf:.2f}', alpha=0.7)
    ax1.axhline(lim_sup, color=ROJO, linestyle='--', linewidth=1,  label=f'Lím.sup = {lim_sup:.2f}', alpha=0.7)
    ax1.set_title(f'Boxplot\n{nombre}', fontsize=11, fontweight='bold', color=AZUL)
    ax1.set_ylabel('Nota', fontsize=10)
    ax1.legend(fontsize=7.5, loc='upper right')
    ax1.yaxis.grid(True, linestyle='--', alpha=0.5, zorder=0)
    ax1.set_xticks([])

    # ── Dispersión ──
    ax2 = axes[1]
    x = np.arange(len(serie))
    y = serie.values
    mask_norm = (y >= lim_inf) & (y <= lim_sup)
    ax2.scatter(x[mask_norm], y[mask_norm], color=color, alpha=0.65, s=40,
                edgecolors='white', linewidth=0.6, label='Normal', zorder=3)
    if (~mask_norm).any():
        ax2.scatter(x[~mask_norm], y[~mask_norm], color=ROJO, alpha=0.9, s=70,
                    marker='X', edgecolors='white', linewidth=0.8, label='Atípico', zorder=4)
    ax2.axhline(lim_sup, color=ROJO,  linestyle='--', linewidth=1.2, alpha=0.7, label=f'Lím.sup {lim_sup:.2f}')
    ax2.axhline(lim_inf, color=ROJO,  linestyle='--', linewidth=1.2, alpha=0.7, label=f'Lím.inf {lim_inf:.2f}')
    ax2.axhline(Q2,      color=DORADO, linestyle='-',  linewidth=1.8, alpha=0.8, label=f'Mediana {Q2:.2f}')
    ax2.set_title(f'Dispersión\n{nombre}', fontsize=11, fontweight='bold', color=AZUL)
    ax2.set_xlabel('Índice estudiante', fontsize=9)
    ax2.set_ylabel('Nota', fontsize=10)
    ax2.legend(fontsize=7.5, loc='upper right')
    ax2.yaxis.grid(True, linestyle='--', alpha=0.45, zorder=0)

    # ── Histograma ──
    ax3 = axes[2]
    counts, edges, patches_h = ax3.hist(serie.dropna(), bins=6,
                                         color=color, alpha=0.7,
                                         edgecolor='white', linewidth=1.2, zorder=3)
    kde_x = np.linspace(serie.min(), serie.max(), 300)
    kde_y = stats.gaussian_kde(serie.dropna())(kde_x) * len(serie) * (edges[1] - edges[0])
    ax3.plot(kde_x, kde_y, color=AZUL, linewidth=2.2, label='KDE (densidad)', zorder=4)
    ax3.axvline(serie.mean(),   color=DORADO, linestyle='-',  linewidth=2,
                label=f'Media {serie.mean():.2f}', zorder=5)
    ax3.axvline(serie.median(), color=ROJO,   linestyle='--', linewidth=1.8,
                label=f'Mediana {serie.median():.2f}', zorder=5)
    for patch, count in zip(patches_h, counts):
        if count > 0:
            ax3.text(patch.get_x() + patch.get_width() / 2, count + 0.3,
                     str(int(count)), ha='center', va='bottom',
                     fontsize=9, fontweight='bold', color=AZUL)
    ax3.set_title(f'Histograma\n{nombre}', fontsize=11, fontweight='bold', color=AZUL)
    ax3.set_xlabel('Nota', fontsize=10)
    ax3.set_ylabel('Frecuencia', fontsize=10)
    ax3.legend(fontsize=8)
    ax3.yaxis.grid(True, linestyle='--', alpha=0.45, zorder=0)

    plt.suptitle(f'Análisis gráfico completo — {nombre}',
                 fontsize=13, fontweight='bold', color=AZUL, y=1.02)
    plt.tight_layout()
    return fig


# ══════════════════════════════════════════════
#  P2 — SECCIÓN 5: ANÁLISIS POR VARIABLE
# ══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🔬 Sección 5 — Análisis por Variable Cuantitativa</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="explain-box">
ℹ️ Para cada una de las 5 variables seleccionadas se presenta:<br>
&nbsp;① <strong>Tabla de frecuencia</strong> con intervalos (<code>pd.cut</code>), frecuencias absolutas, relativas y acumuladas.<br>
&nbsp;② <strong>Estadísticas descriptivas</strong>: media, mediana, moda, desv. estándar, asimetría y curtosis.<br>
&nbsp;③ <strong>Análisis de Tukey</strong>: Q1, Q2, Q3, IQR, límites y detección de valores atípicos.<br>
&nbsp;④ <strong>Gráficas</strong>: Boxplot · Dispersión · Histograma con curva KDE.
</div>
""", unsafe_allow_html=True)

for var in VARIABLES:
    serie  = data[var].dropna()
    nombre = NOMBRES_DISPLAY[var]
    emoji  = EMOJIS[var]
    color  = COLORES_VAR[var]

    st.markdown('<hr class="divider-var">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{emoji} Variable: {nombre}</div>',
                unsafe_allow_html=True)

    # Estadísticas
    media   = serie.mean()
    mediana = serie.median()
    moda    = serie.mode().iloc[0]
    std     = serie.std()
    minv    = serie.min()
    maxv    = serie.max()
    skewv   = float(stats.skew(serie))
    kurtv   = float(stats.kurtosis(serie))

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    for col_widget, label, value, sub in [
        (c1, "Media",      f"{media:.2f}",           "promedio"),
        (c2, "Mediana",    f"{mediana:.2f}",          "Q2 · 50%"),
        (c3, "Moda",       f"{moda:.2f}",             "más frecuente"),
        (c4, "Desv. Std",  f"{std:.2f}",              "dispersión"),
        (c5, "Mín / Máx",  f"{minv:.1f}–{maxv:.1f}", "rango total"),
        (c6, "N",          str(len(serie)),            "estudiantes"),
    ]:
        with col_widget:
            st.markdown(f"""<div class="stat-card">
                <div class="label">{label}</div>
                <div class="value">{value}</div>
                <div class="sub">{sub}</div></div>""", unsafe_allow_html=True)

    # Tabla de frecuencia
    st.markdown(f"**① Tabla de Frecuencia — {nombre}**")
    tabla = tabla_frecuencia_continua(serie, bins=6)
    st.dataframe(tabla, use_container_width=True, hide_index=True)
    st.markdown(f"""
    <div class="explain-box">
    📌 Construida con <code>pd.cut(data["{var}"], bins=6)</code>, dividiendo el rango de notas
    en <strong>6 intervalos de igual amplitud</strong>. La columna <em>F. Rel. Acum. (%)</em>
    muestra el porcentaje acumulado de estudiantes hasta ese intervalo.
    </div>""", unsafe_allow_html=True)

    # Análisis Tukey
    Q1, Q2, Q3, fs, lim_inf, lim_sup, atip_izq, atip_der = analisis_tukey(serie)
    st.markdown(f"**② Cuartiles e IQR — Método de Tukey**")

    cq1, cq2, cq3, cq4, cq5, cq6 = st.columns(6)
    for col_widget, label, value, sub in [
        (cq1, "Q1 (25%)",      f"{Q1:.2f}",      ""),
        (cq2, "Q2 (50%)",      f"{Q2:.2f}",      ""),
        (cq3, "Q3 (75%)",      f"{Q3:.2f}",      ""),
        (cq4, "IQR (fs)",      f"{fs:.2f}",      ""),
        (cq5, "Lím. Inferior", f"{lim_inf:.2f}", "Q1 − 1.5·IQR"),
        (cq6, "Lím. Superior", f"{lim_sup:.2f}", "Q3 + 1.5·IQR"),
    ]:
        with col_widget:
            st.markdown(f"""<div class="stat-card">
                <div class="label">{label}</div>
                <div class="value">{value}</div>
                <div class="sub">{sub}</div></div>""", unsafe_allow_html=True)

    total_atip = len(atip_izq) + len(atip_der)
    if total_atip == 0:
        st.markdown(f"""<div class="alert-box-green">
        ✅ <strong>Sin valores atípicos</strong> — Todos los datos de <em>{nombre}</em>
        están dentro del rango [{lim_inf:.2f}, {lim_sup:.2f}].
        </div>""", unsafe_allow_html=True)
    else:
        partes = []
        if len(atip_izq) > 0: partes.append(f"• Por debajo del límite inferior: {len(atip_izq)} dato(s).")
        if len(atip_der) > 0: partes.append(f"• Por encima del límite superior: {len(atip_der)} dato(s).")
        st.markdown(f"""<div class="alert-box-red">
        ⚠️ <strong>{total_atip} valor(es) atípico(s)</strong> detectado(s) en <em>{nombre}</em>
        fuera del rango [{lim_inf:.2f}, {lim_sup:.2f}].<br>{"<br>".join(partes)}
        </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="explain-box">
    📐 <strong>Asimetría (skewness):</strong> {skewv:.4f} → {tipo_asimetria(skewv)}<br>
    📐 <strong>Curtosis (Fisher):</strong> {kurtv:.4f} → {tipo_curtosis(kurtv)}<br><br>
    El <strong>IQR = {fs:.2f}</strong> representa la amplitud del 50 % central de los datos.
    Valores fuera de [{lim_inf:.2f}, {lim_sup:.2f}] se consideran atípicos según Tukey
    (Q1 − 1.5·IQR y Q3 + 1.5·IQR).
    </div>""", unsafe_allow_html=True)

    # Gráficas
    st.markdown(f"**③ Visualizaciones — Boxplot · Dispersión · Histograma**")
    fig = graficar_trio(serie, nombre, color, Q1, Q2, Q3, lim_inf, lim_sup, atip_izq, atip_der)
    st.pyplot(fig)

    st.markdown(f"""
    <div class="explain-box">
    🔍 <strong>Lectura de las gráficas:</strong><br>
    &nbsp;• <strong>Boxplot:</strong> la caja va del Q1 ({Q1:.2f}) al Q3 ({Q3:.2f}),
    línea dorada = mediana ({Q2:.2f}). Puntos rojos ✕ = atípicos.<br>
    &nbsp;• <strong>Dispersión:</strong> cada punto es un estudiante. Los ✕ rojos caen
    fuera de [{lim_inf:.2f}, {lim_sup:.2f}].<br>
    &nbsp;• <strong>Histograma:</strong> barras = frecuencia por intervalo, línea azul = KDE,
    línea dorada = media ({media:.2f}), línea roja = mediana ({mediana:.2f}).
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  P2 — SECCIÓN 6: RESUMEN COMPARATIVO
# ══════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">📊 Sección 6 — Resumen Comparativo de las 5 Variables</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="explain-box">
ℹ️ La siguiente tabla resume las métricas clave de las 5 variables analizadas, permitiendo
comparar de un vistazo la distribución de notas entre las diferentes materias.
</div>
""", unsafe_allow_html=True)

resumen_rows = []
for var in VARIABLES:
    serie = data[var].dropna()
    Q1, Q2, Q3, fs, lim_inf, lim_sup, atip_izq, atip_der = analisis_tukey(serie)
    resumen_rows.append({
        'Variable':    NOMBRES_DISPLAY[var],
        'Media':       round(serie.mean(), 3),
        'Mediana':     round(serie.median(), 3),
        'Desv. Std':   round(serie.std(), 3),
        'Q1':          round(Q1, 3),
        'Q3':          round(Q3, 3),
        'IQR':         round(fs, 3),
        'Lím. Inf.':   round(lim_inf, 3),
        'Lím. Sup.':   round(lim_sup, 3),
        'Atípicos':    len(atip_izq) + len(atip_der),
        'Asimetría':   round(float(stats.skew(serie)), 3),
        'Curtosis':    round(float(stats.kurtosis(serie)), 3),
    })

resumen_df = pd.DataFrame(resumen_rows)
st.dataframe(resumen_df.set_index('Variable'), use_container_width=True)

# Boxplots comparativos
st.markdown("**Boxplots comparativos — las 5 materias en un solo gráfico**")

fig_comp, ax_comp = plt.subplots(figsize=(14, 6))
fig_comp.patch.set_facecolor('#f7fafd')
ax_comp.set_facecolor('#f0f6fc')

data_bp = [data[v].dropna().values for v in VARIABLES]
labels  = [NOMBRES_DISPLAY[v] for v in VARIABLES]
colores = [COLORES_VAR[v] for v in VARIABLES]

bp = ax_comp.boxplot(data_bp, labels=labels, patch_artist=True, widths=0.5,
                     medianprops=dict(color=DORADO, linewidth=3),
                     whiskerprops=dict(linewidth=1.8, linestyle='--'),
                     capprops=dict(linewidth=2.5),
                     flierprops=dict(marker='o', markersize=6, alpha=0.8))

for patch, color in zip(bp['boxes'], colores):
    patch.set_facecolor(color); patch.set_alpha(0.5)
for whisker, color in zip(bp['whiskers'], [c for c in colores for _ in range(2)]):
    whisker.set_color(color)
for cap, color in zip(bp['caps'], [c for c in colores for _ in range(2)]):
    cap.set_color(color)
for flier in bp['fliers']:
    flier.set_markerfacecolor(ROJO); flier.set_markeredgecolor(ROJO)

ax_comp.axhline(3.0, color=ROJO, linestyle='--', linewidth=1.5, alpha=0.6,
                label='Nota mínima aprobatoria (3.0)')
ax_comp.set_ylabel('Nota', fontsize=11, fontweight='bold')
ax_comp.set_title('Comparación de Distribución de Notas — 5 Materias',
                  fontsize=13, fontweight='bold', color=AZUL, pad=12)
ax_comp.yaxis.grid(True, linestyle='--', alpha=0.45, zorder=0)
ax_comp.legend(fontsize=10)
plt.xticks(rotation=20, ha='right', fontsize=10)
plt.tight_layout()
st.pyplot(fig_comp)

st.markdown("""
<div class="explain-box">
📌 <strong>Lectura del gráfico comparativo:</strong> cada caja representa una materia.
La línea dorada interior es la mediana. Las cajas más altas indican mayor dispersión en las notas.
La línea roja punteada marca <strong>3.0</strong> (nota mínima aprobatoria en Colombia).
Las materias cuya caja cae mayoritariamente por encima de 3.0 tienen mejor rendimiento global.
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#9ecae8; font-size:0.82rem; padding:0.5rem 0 1rem 0;
     font-family:'IBM Plex Mono', monospace;">
    Taller #1 · Completo · Estadística 3 · Ingeniería de Sistemas
</div>
""", unsafe_allow_html=True)