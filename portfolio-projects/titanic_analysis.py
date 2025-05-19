import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veri setini yükle
df = sns.load_dataset("titanic")

# Temel bilgi
print(df.info())

# Hayatta kalanların cinsiyete göre dağılımı
sns.countplot(x="sex", hue="survived", data=df)
plt.title("Survival by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()
