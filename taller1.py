import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

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
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-banner">
    <h1>📊 Taller #1 &mdash; Estadística 3</h1>
    <p class="meta">Carrera: &nbsp;<strong>Ingeniería de Sistemas</strong></p>
    <p class="meta">Estudiante: &nbsp;<span class="name-field">Andres Felipe Velez Alcaraz</span></p>
    <p class="meta">Profesor: &nbsp;<span class="name-field">Daniel Betancur Trujillo</span></p>
    <p class="meta">Tema: Tablas de Frecuencia · Gráficas de Pareto · Gráfica Radar Cruzada (Municipio × EPS)</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LIBRERÍAS
# ─────────────────────────────────────────────
with st.expander("📦 Librerías utilizadas en este taller", expanded=False):
    st.markdown("""
    <div style="padding:0.5rem 0">
    <span class="lib-pill">pandas</span>
    <span class="lib-pill">matplotlib</span>
    <span class="lib-pill">numpy</span>
    <span class="lib-pill">streamlit</span>
    </div>

    | Librería | Descripción |
    |---|---|
    | **pandas** | Manipulación y análisis de datos tabulares. Permite leer CSV, crear DataFrames, tablas cruzadas (`pd.crosstab`) y calcular estadísticas con pocas líneas de código. |
    | **matplotlib** | Librería de visualización 2D de Python. Base del ecosistema científico de gráficas; usada aquí para los diagramas de Pareto y la gráfica radar. |
    | **numpy** | Computación numérica vectorial. Se usa para calcular los ángulos equidistantes de la gráfica radar con `np.linspace`. |
    | **streamlit** | Framework que convierte scripts Python en aplicaciones web interactivas sin HTML/CSS/JS adicional. Ideal para presentaciones académicas y dashboards de datos. |
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CARGA DE DATOS
# Lee el CSV desde la misma carpeta donde está taller1.py
# ─────────────────────────────────────────────
st.markdown('<div class="section-title">📂 Datos cargados — 04 - estudiantes.csv</div>',
            unsafe_allow_html=True)

df = pd.read_csv("04 - estudiantes.csv")

st.dataframe(df, use_container_width=True)
st.caption(f"Total registros: {len(df)} estudiantes · {len(df.columns)} variables")

# ─────────────────────────────────────────────
# PALETA DE COLORES
# ─────────────────────────────────────────────
AZUL        = '#1b3a5c'
DORADO      = '#f0a500'
ROJO_PARETO = '#e63946'
PALETA      = ['#1b3a5c','#f0a500','#4a7fa5','#e8a020',
               '#88bbd8','#f7c948','#c9e2f0','#0d2b45',
               '#2e86ab','#a23b72','#f18f01','#c73e1d']

# ─────────────────────────────────────────────
# HELPER — tabla de frecuencia simple
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
# HELPER — gráfica de Pareto reutilizable
# ─────────────────────────────────────────────
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


# ══════════════════════════════════════════════════════════
#  SECCIÓN 1 — PARETO: MUNICIPIO DE RESIDENCIA
# ══════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🏙️ Sección 1 — Pareto: Municipio de Residencia</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="explain-box">
ℹ️ <strong>¿Qué es la gráfica de Pareto?</strong><br>
Combina barras ordenadas de mayor a menor (frecuencia absoluta) con una línea de frecuencia
relativa acumulada. Permite identificar rápidamente las categorías que concentran la mayor parte
de los datos. La línea punteada roja en el 80 % ilustra el principio de Pareto: las pocas
categorías "vitales" frente a las muchas "triviales".<br><br>
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


# ══════════════════════════════════════════════════════════
#  SECCIÓN 2 — PARETO: EPS
# ══════════════════════════════════════════════════════════
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

fig_eps = grafica_pareto(pareto_eps, 'EPS',
                          'Diagrama de Pareto — EPS', ancho=9)
st.pyplot(fig_eps)


# ══════════════════════════════════════════════════════════
#  SECCIÓN 3 — TABLA CRUZADA: MUNICIPIO × EPS
# ══════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🔀 Sección 3 — Tabla Cruzada: Municipio × EPS</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="explain-box">
ℹ️ <strong>¿Qué es una tabla cruzada?</strong><br>
Es una tabla de doble entrada que cruza dos variables categóricas usando <code>pd.crosstab()</code>.
Las <strong>filas</strong> son los municipios de residencia, las <strong>columnas</strong> son cada EPS,
y cada celda indica <em>cuántos estudiantes de ese municipio están afiliados a esa EPS</em>.
El valor <strong>0</strong> significa que ningún estudiante de ese municipio pertenece a esa EPS.
La columna <strong>TOTAL</strong> suma todos los estudiantes por municipio y la fila
<strong>TOTAL</strong> suma todos por EPS.<br><br>
Esta tabla es exactamente la fuente de datos que alimenta la gráfica de radar de la siguiente sección.
</div>
""", unsafe_allow_html=True)

tabla_cruzada = pd.crosstab(
    df['Municipio_Residencia'],
    df['EPS'],
    margins=True,
    margins_name='TOTAL'
)
tabla_cruzada.index.name = 'Municipio \\ EPS'

st.dataframe(tabla_cruzada, use_container_width=True)

st.markdown("""
<div class="explain-box">
📌 <strong>Ejemplo de lectura:</strong> busca la fila de un municipio y recorre sus columnas
para ver cuántos estudiantes de allí están en Coosalud, Sanitas, Salud Total, etc.
La fila <em>TOTAL</em> te dice cuántos estudiantes hay por EPS en todo el grupo.
La columna <em>TOTAL</em> te dice cuántos estudiantes hay por municipio en total.
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
#  SECCIÓN 4 — GRÁFICA RADAR: MUNICIPIO × EPS
# ══════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<div class="section-title">🕸️ Sección 4 — Gráfica Radar: Municipio × EPS</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="explain-box">
ℹ️ <strong>¿Qué muestra esta gráfica radar?</strong><br>
Cada <strong>eje</strong> corresponde a un municipio de residencia. La distancia desde el
centro hasta un vértice indica cuántos estudiantes de ese municipio pertenecen a una EPS,
medida en <strong>valores absolutos reales</strong> (número de estudiantes).<br><br>
Cada <strong>polígono coloreado</strong> representa una EPS distinta. Su forma revela el
patrón de distribución geográfica de sus afiliados:<br>
&nbsp;• Polígono <strong>grande y uniforme</strong> → la EPS tiene afiliados repartidos
de forma similar en todos los municipios.<br>
&nbsp;• Polígono <strong>con picos en ciertos ejes</strong> → la EPS concentra sus afiliados
en esos municipios específicos.<br>
&nbsp;• Polígono <strong>pequeño o hundido en un eje</strong> → la EPS tiene pocos o ningún
afiliado en ese municipio.<br><br>
La escala va de <strong>0 a 113</strong> (el valor máximo real encontrado en toda la tabla),
lo que permite comparar directamente todas las EPS y todos los municipios en la misma
referencia sin distorsión por normalización.
</div>
""", unsafe_allow_html=True)

# ── Preparar datos: ejes = municipios, líneas = EPS ──
radar_df   = tabla_cruzada.drop(index='TOTAL')
eps_lista  = [c for c in radar_df.columns if c != 'TOTAL']
municipios = list(radar_df.index)

N      = len(municipios)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]                                   # cerrar polígono

# Escala fija: 0 al máximo global de la tabla (sin columna TOTAL)
MAX_ESCALA = int(radar_df[eps_lista].values.max())     # 113 según los datos reales

fig_radar, ax_r = plt.subplots(figsize=(11, 10), subplot_kw=dict(polar=True))
ax_r.set_facecolor('#f0f6fc')
fig_radar.patch.set_facecolor('#f7fafd')

for i, eps in enumerate(eps_lista):
    vals  = [int(radar_df.loc[m, eps]) for m in municipios]
    vals += vals[:1]                                   # cerrar polígono
    color = PALETA[i % len(PALETA)]
    ax_r.plot(angles, vals, color=color, linewidth=2.2, label=eps)
    ax_r.fill(angles, vals, color=color, alpha=0.10)

    # Etiqueta del valor real en cada vértice
    for ang, val in zip(angles[:-1], vals[:-1]):
        if val > 0:
            ax_r.annotate(
                str(val),
                xy=(ang, val),
                xytext=(ang, val + MAX_ESCALA * 0.04),
                fontsize=6.5, color=color, fontweight='bold',
                ha='center', va='bottom'
            )

# Etiquetas de los ejes = municipios
ax_r.set_xticks(angles[:-1])
ax_r.set_xticklabels(municipios, fontsize=9, color=AZUL, fontweight='bold')

# Escala absoluta de 0 a MAX_ESCALA
paso = 20
ticks_vals = list(range(0, MAX_ESCALA + paso, paso))
ax_r.set_ylim(0, MAX_ESCALA + 10)
ax_r.set_yticks(ticks_vals)
ax_r.set_yticklabels([str(v) for v in ticks_vals], fontsize=7, color='gray')

ax_r.set_title(
    f'Gráfica Radar — Estudiantes por EPS en cada Municipio\n'
    f'(ejes = municipios · cada polígono = una EPS · escala: 0 – {MAX_ESCALA} estudiantes)',
    fontsize=11, fontweight='bold', color=AZUL, pad=32
)
ax_r.legend(loc='upper right', bbox_to_anchor=(1.6, 1.2),
            fontsize=9, title='EPS', title_fontsize=10)
ax_r.grid(color='#c0d8f0', linestyle='--', linewidth=0.8)

plt.tight_layout()
st.pyplot(fig_radar)

st.markdown(f"""
<div class="explain-box">
📌 <strong>Cómo leer la gráfica paso a paso:</strong><br>
1. Elige una <strong>EPS</strong> en la leyenda (derecha) e identifica su color.<br>
2. Localiza su polígono y observa qué ejes (municipios) alcanza más lejos desde el centro.<br>
3. El número anotado en cada vértice es la cantidad exacta de estudiantes de ese municipio
   afiliados a esa EPS.<br>
4. Compara los polígonos entre sí: una EPS cuyo polígono envuelve a otro tiene más afiliados
   en esos municipios.<br><br>
<strong>Escala fija 0 – {MAX_ESCALA}:</strong> al usar la misma escala para todas las EPS y
municipios, los valores son directamente comparables. Un vértice que llega a 113 (máximo)
representa la combinación municipio-EPS con más estudiantes de todo el grupo.
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#9ecae8; font-size:0.82rem; padding:0.5rem 0 1rem 0;
     font-family:'IBM Plex Mono', monospace;">
    Taller #1 · Estadística 3 · Ingeniería de Sistemas
</div>
""", unsafe_allow_html=True)