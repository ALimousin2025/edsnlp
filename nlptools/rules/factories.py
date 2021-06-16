from typing import Dict, List

from spacy.language import Language

from nlptools.rules.pollution import Pollution, terms as pollution_terms
from nlptools.rules.sections import Sections, terms as section_terms
from nlptools.rules.quickumls import QuickUMLSComponent

pollution_default_config = dict(
    pollution=pollution_terms.pollution,
)


# noinspection PyUnusedLocal
@Language.factory("pollution", default_config=pollution_default_config)
def create_pollution_component(
        nlp: Language,
        name: str,
        pollution: Dict[str, str],
):
    return Pollution(nlp, pollution=pollution)


sections_default_config = dict(
    sections=section_terms.sections,
)


# noinspection PyUnusedLocal
@Language.factory("sections", default_config=sections_default_config)
def create_sections_component(
        nlp: Language,
        name: str,
        sections: Dict[str, List[str]],
):
    return Sections(nlp, sections=sections)


# noinspection PyUnusedLocal
@Language.factory("quickumls")
def create_quickumls_component(
        nlp: Language,
        name: str,
        distribution: str,
):
    return QuickUMLSComponent(nlp, distribution=distribution)
