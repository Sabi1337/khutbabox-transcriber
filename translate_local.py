import argostranslate.package
import argostranslate.translate


def übersetze_offline(text, von="tr", nach="de"):
    installed = argostranslate.translate.get_installed_languages()
    from_lang = next((l for l in installed if l.code == von), None)
    to_lang = next((l for l in installed if l.code == nach), None)

    if not from_lang or not to_lang:
        return "⚠️ Übersetzung nicht möglich – Sprachpaket fehlt."

    return from_lang.get_translation(to_lang).translate(text)
