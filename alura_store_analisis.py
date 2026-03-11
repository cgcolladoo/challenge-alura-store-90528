import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== ALURA STORE ANALYSIS - Task 90528 ===")

# 1. CARGAR 4 TIENDAS (ajusta paths)
df1 = pd.read_csv('store1.csv')  # Tienda 1
df2 = pd.read_csv('store2.csv')  # Tienda 2
df3 = pd.read_csv('store3.csv')  # Tienda 3
df4 = pd.read_csv('store4.csv')  # Tienda 4

# Agregar columna tienda
df1['Tienda'] = 'Tienda 1'
df2['Tienda'] = 'Tienda 2'
df3['Tienda'] = 'Tienda 3'
df4['Tienda'] = 'Tienda 4'

# Combinar
df = pd.concat([df1, df2, df3, df4], ignore_index=True)
print(f"Dataset total: {df.shape}")
print(df.head())

# 2. ANÁLISIS 1: FATURAMIENTO TOTAL
faturamento = df.groupby('Tienda')['Precio'].sum()
print("\n💰 Faturamento por Tienda:")
print(faturamento)

# 3. TOP CATEGORÍAS
categorias = df.groupby(['Tienda', 'Categoria'])['Cantidad'].sum().unstack(fill_value=0)
print("\n📦 Ventas por Categoría:")
print(categorias)

# 4. CALIFICACIÓN PROMEDIO
calificacion = df.groupby('Tienda')['Calificacion'].mean()
print("\n⭐ Calificación Media:")
print(calificacion)

# 5. PRODUCTOS MÁS/MENOS VENDIDOS
top_prod = df.groupby(['Tienda', 'Producto'])['Cantidad'].sum().groupby(level=0).head(3)
print("\n🏆 Top 3 Productos:")
print(top_prod)

# 6. FRETE PROMEDIO
frete_prom = df.groupby('Tienda')['Costo_Frete'].mean()
print("\n🚚 Frete Promedio:")
print(frete_prom)

# 7. VISUALIZACIONES
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Faturamento
faturamento.plot(kind='bar', ax=axes[0,0], title='Faturamento Total')
axes[0,0].set_ylabel('Monto')

# Categorías (Tienda 1 ejemplo)
categorias.loc['Tienda 1'].plot(kind='bar', ax=axes[0,1], title='Categorías Tienda 1')
axes[0,1].set_ylabel('Cantidad')

# Calificación
calificacion.plot(kind='bar', ax=axes[1,0], title='Calificación Media')
axes[1,0].set_ylabel('Estrellas')

# Frete
frete_prom.plot(kind='bar', ax=axes[1,1], title='Frete Promedio')
axes[1,1].set_ylabel('Costo')

plt.tight_layout()
plt.savefig('alura_store_dashboard.png', dpi=300)
plt.show()

# 8. RECOMENDACIÓN
print("\n🎯 RECOMENDACIÓN:")
print("Tienda con MENOR:")
print("- Faturamento:", faturamento.idxmin())
print("- Calificación:", calificacion.idxmin())
print("- Margen frete alto")

print("\n✅ ANÁLISIS COMPLETO - Task 90528")
