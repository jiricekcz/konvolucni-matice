# {Název úkolu}

## Spuštění

```bash
python3 ./src/main.py "{INPUT_FILE}" "{OUTPUT_FILE}"
```

## Popis Funkce

Program načte konvoluční matici ze souboru `./resources/options.json` a vstupní obrázek ze souboru `{INPUT_FILE}`. Výsledný obrázek uloží do souboru `{OUTPUT_FILE}`.  
Pokud není zadán výstupní soubor, výsledek se uloží do souboru se stejným názvem jako vstupní soubor, ale s příponou `_new` (např. `input.png` -> `input_new.png`).
Limit kánálů v souboru `./resources/options.json` určuje, na kolika kanálech proběhne konvoluce. Pokud je limit 3, program provede konvoluci pouze na prvních třech kanálech (RGB). Pokud je limit 4, program provede konvoluci na všech čtyřech kanálech (RGBA). Provádění konvoluce na alfa kanálu může způsobit, že obrázek nebude vidět, i přestože průhlednost je nastavena na 100%, pokud je suma hodnot v konvoluční matici menší než 1.  
  
Kovoluce probíhá kompletně v pythonu, čili trvá relativně dlouho. Pokud je vstupní obrázek velký, může trvat i několik minut.
