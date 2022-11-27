# **Cíl** 
Vytvořit program, který bude bude provádět konvoluci 3x3 s obrázkem.

# **Podrobnější popis** 
V GIMPu jsme pracovali s konvolučními filtry, nyní si takový filtr sami naprogramujeme. Pro připomenutí odkaz na vysvětlení konvoluce a jejích efektů - https://docs.gimp.org/2.6/en/plug-in-convmatrix.html. Jádro programu bude funkce, která jako vstup dostane matici obrázku a matici konvolučního filtru (obě ve formátu numpy array). Pokud nevíte, co je numpy array, tak se na to můžete koukat jako na lepší pythoní list. Uvnitř této funkce se provede konvoluce a funkce vrátí jako výstup matici, ve které je uložený obrázek. Jakmile budete mít tuto funkci hotovou, tak stačí dodělat načtení obrázku a poté jeho uložení.

Pro načtení obrázku doporučuji  
```python
from matplotlib.image import imread 
image = imread("obrazek.png")
```
Pro uložení
```python
import matplotlib.pyplot as plt
plt.imsave('output.png', matice_obrazku_k_ulozeni)
```
 Tím, že budete pracovat s numpy polem, získáte spoustu výhod:

- Obrázek se dá zkopírovat jako: newImg = image.copy()
- Pokud máte pixel, který obsahuje 3 kanály (r,g,b) (takže vypadá jako p1=[r,g,b]) a chtěli byste k němu přičíst jiný pixel p2=[x,y,z], tak to funguje pěkně - p3 = p1+p2 udělá [r+x,g+y,b+z].
- Pokud byste chtěli takový pixel přenásobit třeba 2, tak se vynásobí po jednotlivých elementech. p1=[r,g,b] a pro p2=p1*2 získám [2r,2g,2b]. Toho můžete využít, když nebudete chtít dělat konvoluci pro každý kanál zvlášť.

Ještě jedna poznámka - některé obrázky mají 4 kanály (r,g,b,alpha), kde alpha udává průhlednost. Obrázek, který vám posílám a na kterém si to můžete zkoušet, má 3, ale je to jenom upozornění, kdybyste chtěli experimentovat.
Další informace - místo barev 0-255 pro každý RGB kanál se častěji používá desetinné číslo 0..1 pro vyjádření, kolik tam které barvy je (0.0 odpovídá 0 a 1.0 odpovídá 255).

Může se stát, že při úpravách konvoluční matice se vám některý pixel může zvětšit nad 1, nebo naopak zmenšit pod 0. Takovou matici by vám potom program nechtěl uložit, takže je potřeba takové hodnoty oříznout. Například takto:
matice[matice>1]=1  ... všechny prvky větší než 1 nastaví na 1
matice[matice<0]=0  ... všechny prvky menší než 0 nastaví na 0

Ač se to takto může zdát trochu děsivé, tak samotný program vůbec nebude dlouhý a složitý - funkce umí být při vhodné implementaci na 15 řádků a zbytek programu na dalších 15. Zkuste se tedy do toho pustit :). A kdybyste nevěděli nebo se zasekli, tak mi napište :).


# **Spolupráce, zdroje, internet**
Práci byste měli vypracovat samostatně, protože za ní budete hodnoceni. Je v pořádku se bavit o řešení se spolužáky, ale kód byste pak měli napsat sami (pokud vám něco nefunguje a někdo vám pomůže opravit chybu, tak to je samozřejmě také v pořádku). Není v pořádku nechat za sebe práci vypracovat někým jiným. Můžete používat internet a vyhledávat věci, ale pokud odněkud zkopírujete část kódu, měli byste ji označit. Je v pořádku stáhnout například funkci pro generování náhodného šumu, není v pořádku stáhnout celý program.

# **Hodnocení**
Budu způsob provedení, kvalitu kódu (jak je to pěkně napsané, komentáře, členění do funkcí apod.). Jinými slovy - budu hodnotit cestu, jakou jste k výsledku přišli, nikoliv jen samotný výsledek, protože je mým cílem vás naučit pěknému způsobu řešení problémů (tedy obecnému postupu), nikoliv hodnotit výsledek, který vytvoříte.

# **Co odevzdat**  
Odevzdejte kód v Pythonu a k němu samostatný textový dokument, kde popíšete, jak program použít (jak pojmenovat obrázek a kam ho uložit atd.)

# **JAK ODEVZDAT**  
Součástí hodnocení bude i správně napsaný předmět v emailu. Tedy 7M - úkol - konvoluce.


**Termín odevzdání**: `28. 11. 2022`
