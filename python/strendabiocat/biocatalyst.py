"""
This file contains Pydantic model definitions for data validation.

Pydantic is a data validation library that uses Python type annotations.
It allows you to define data models with type hints that are validated
at runtime while providing static type checking.

Usage example:
```python
from my_model import MyModel

# Validates data at runtime
my_model = MyModel(name="John", age=30)

# Type-safe - my_model has correct type hints
print(my_model.name)

# Will raise error if validation fails
try:
    MyModel(name="", age=30)
except ValidationError as e:
    print(e)
```

For more information see:
https://docs.pydantic.dev/

WARNING: This is an auto-generated file.
Do not edit directly - any changes will be overwritten.
"""


## This is a generated file. Do not modify it manually!

from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Generic, TypeVar, Union
from enum import Enum
from uuid import uuid4
from datetime import date, datetime

# Filter Wrapper definition used to filter a list of objects
# based on their attributes
Cls = TypeVar("Cls")


class FilterWrapper(Generic[Cls]):
    """Wrapper class to filter a list of objects based on their attributes"""

    def __init__(self, collection: list[Cls], **kwargs):
        self.collection = collection
        self.kwargs = kwargs

    def filter(self) -> list[Cls]:
        for key, value in self.kwargs.items():
            self.collection = [
                item for item in self.collection if self._fetch_attr(key, item) == value
            ]
        return self.collection

    def _fetch_attr(self, name: str, item: Cls):
        try:
            return getattr(item, name)
        except AttributeError:
            raise AttributeError(f"{item} does not have attribute {name}")


# JSON-LD Helper Functions
def add_namespace(obj, prefix: str | None, iri: str | None):
    """Adds a namespace to the JSON-LD context

    Args:
        prefix (str): The prefix to add
        iri (str): The IRI to add
    """
    if prefix is None and iri is None:
        return
    elif prefix and iri is None:
        raise ValueError("If prefix is provided, iri must also be provided")
    elif iri and prefix is None:
        raise ValueError("If iri is provided, prefix must also be provided")

    obj.ld_context[prefix] = iri  # type: ignore


def validate_prefix(term: str | dict, prefix: str):
    """Validates that a term is prefixed with a given prefix

    Args:
        term (str): The term to validate
        prefix (str): The prefix to validate against

    Returns:
        bool: True if the term is prefixed with the prefix, False otherwise
    """

    if isinstance(term, dict) and not term["@id"].startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")
    elif isinstance(term, str) and not term.startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")


# Model Definitions


class BiocatalystPurchased(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    name: str = Field(
        default=...,
        description="""The name of the biocatalyst can be either generic
        based on the catalyzed reaction, for
        example, 'lipase' or more specifically
        by describing the genus and species, such
        as ' Bacillus amyloliquefaciens alpha-
        amylase'.""",
    )
    ec_number: str = Field(
        default=...,
        description="""Numerical classification system that categorizes
        enzymes based on their biochemical
        function and reaction mechanism, such as
        EC 3.1.4.12.""",
    )
    molecular_weight: float = Field(
        default=...,
        description="""The molecular weight (MW) refer to the sum of the
        atomic weights of the atoms in a molecule
        and therefore describes the mass of an
        enzyme.""",
    )
    molecular_weight_unit: str = Field(
        default=...,
        description="""The enzyme size or molar weight is typically
        expressed in kDa (kilodaltons).""",
    )
    catalyzed_reaction: str = Field(
        default=...,
        description="""The reaction catalyzed by the biocatalyst.""",
    )
    sequence_amino_acid: str = Field(
        default=...,
        description="""The amino acid sequence of the biocatalyst. The
        amino acid sequence can be represented in
        either a three-letter or one-letter code.
        For instance, "Ala-Ser-Gly" corresponds
        to the three-letter code, while "ASG"
        represents the same sequence in the one-
        letter code. One of the databases commonly
        used for storing and retrieving amino
        acid sequences is the UniProt database
        (https://www.uniprot.org/). UniProt
        provides extensive information on protein
        sequences, including their one-letter and
        three-letter amino acid codes, allowing
        researchers to access and analyze various
        protein sequences.""",
    )
    sequence_DNA: str = Field(
        default=...,
        description="""The DNA sequence of the biocatalyst including any
        tags and linkers.""",
    )
    origin_organism: str = Field(
        default=...,
        description="""The specific species or source from which the
        enzyme is derived or isolated. It includes
        information about the genus and species of
        the organism. However, the cell type from
        which the biocatalyst is derived could be
        bacterial, as well as plant, animal, or
        other sources. ( if_applicable )""",
    )
    supplier: str = Field(
        default=...,
        description="""Information about the supplier from which the
        enzyme was purchased. If possible, a
        reference for the purchased biocatalyst
        should also be provided.""",
    )
    production_organism: str = Field(
        default=...,
        description="""Information about the organism in which the
        biocatalyst was produced is crucial in the
        context of heterologous gene expression.""",
    )
    posttranslational_modification: str = Field(
        default=...,
        description="""Information about any chemical modifications
        or alterations that occur to the
        biocatalyst's protein structure after
        translation, such as phosphorylation,
        glycosylation, acetylation, methylation,
        ubiquitination and other modifications.""",
    )
    purity: float = Field(
        default=...,
        description="""Purity of enzymes typically expressed in
        percentage (%). It is usually stated
        as the percentage of the pure enzyme or
        active component relative to the total
        mass of the enzyme preparation.""",
    )
    purity_specification: str = Field(
        default=...,
        description="""Description of how the purity of the biocatalyst
        was determined. In case of purchased
        enzymes, this information is often
        available from the product specification
        sheet.""",
    )
    formulation: str = Field(
        default=...,
        description="""Depending on the formulation, the biocatalyst
        can exist either in a dissolved state
        within a solvent or as a solid powder.
        It defines the physical state in which
        the biocatalyst is used. Additional
        information regarding the application or
        formulation in the experiment should be
        entered in the next subcategory.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:BiocatalystPurchased/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:BiocatalystPurchased",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class BiocatalystSelfProduced(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    name: str = Field(
        default=...,
        description="""The name of the biocatalyst can be either generic
        based on the catalyzed reaction, for
        example, 'lipase' or more specifically
        by describing the genus and species, such
        as ' Bacillus amyloliquefaciens alpha-
        amylase'.""",
    )
    ec_number: str = Field(
        default=...,
        description="""Numerical classification system that categorizes
        enzymes based on their biochemical
        function and reaction mechanism, such as
        EC 3.1.4.12.""",
    )
    molecular_weight: float = Field(
        default=...,
        description="""The molecular weight (MW) refer to the sum of the
        atomic weights of the atoms in a molecule
        and therefore describes the mass of an
        enzyme.""",
    )
    molecular_weight_unit: str = Field(
        default=...,
        description="""The enzyme size or molar weight is typically
        expressed in kDa (kilodaltons).""",
    )
    catalyzed_reaction: str = Field(
        default=...,
        description="""The reaction catalyzed by the biocatalyst.""",
    )
    sequence_amino_acid: str = Field(
        default=...,
        description="""The amino acid sequence of the biocatalyst. The
        amino acid sequence can be represented in
        either a three-letter or one-letter code.
        For instance, "Ala-Ser-Gly" corresponds
        to the three-letter code, while "ASG"
        represents the same sequence in the one-
        letter code. One of the databases commonly
        used for storing and retrieving amino
        acid sequences is the UniProt database
        (https://www.uniprot.org/). UniProt
        provides extensive information on protein
        sequences, including their one-letter and
        three-letter amino acid codes, allowing
        researchers to access and analyze various
        protein sequences.""",
    )
    sequence_DNA: str = Field(
        default=...,
        description="""The DNA sequence of the biocatalyst including any
        tags and linkers.""",
    )
    sequence_plasmid: str = Field(
        default=...,
        description="""The DNA sequence of the plasmid used to produce
        the biocatalyst. The sequence can be
        provided in plain text or as a database
        ID.""",
    )
    plasmid_specifications: str = Field(
        default=...,
        description="""All DNA sequence changes (e.g. codon optimization
        for E. coli , insertion of affinity
        tags, sequence truncation, etc.) should
        be provided.""",
    )
    origin_organism: str = Field(
        default=...,
        description="""The specific species or source from which the
        enzyme is derived or isolated. It includes
        information about the genus and species of
        the organism. ( if_applicable )""",
    )
    production_organism: str = Field(
        default=...,
        description="""Information about the organism in which the
        biocatalyst was produced is crucial
        in the context of heterologous gene
        expression. If the production strain was
        purchased, more detailed information on
        the manufacturer and the organism should
        be provided.""",
    )
    posttranslational_modification: str = Field(
        default=...,
        description="""Information about any chemical modifications
        or alterations that occur to the
        biocatalyst's protein structure after
        translation, such as phosphorylation,
        glycosylation, acetylation, methylation,
        ubiquitination and other modifications.""",
    )
    purity: float = Field(
        default=...,
        description="""Purity of enzymes typically expressed in
        percentage (%). It is usually stated
        as the percentage of the pure enzyme or
        active component relative to the total
        mass of the enzyme preparation.""",
    )
    purity_specification: str = Field(
        default=...,
        description="""The choice of method for the purity determination
        depends on the type of enzyme and the
        available resources and may include gel
        electrophoresis, HPLC, ELISA, Western
        blotting, etc.""",
    )
    purification_method: str = Field(
        default=...,
        description="""The choice of purification methods is diverse
        and can impact the enzyme, with possible
        methods including chromatographic
        techniques, precipitation, HPLC,
        ultrafiltration, dialysis, salt
        fractionation, etc.""",
    )
    formulation: str = Field(
        default=...,
        description="""Depending on the formulation, the biocatalyst
        can exist either in a dissolved state
        within a solvent or as a solid powder.
        It defines the physical state in which
        the biocatalyst is used. Additional
        information regarding the application or
        formulation in the experiment should be
        entered in the next subcategory.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:BiocatalystSelfProduced/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:BiocatalystSelfProduced",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class PurifiedBiocatalyst(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    concentration: float = Field(
        default=...,
        description="""Concentration of the biocatalyst.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""Concentration of the biocatalyst is typically
        expressed in g/L (grams per liter).""",
    )
    concentration_determination_method: str = Field(
        default=...,
        description="""It is important to specify the method used
        for concentration determination. There
        are various methods available for the
        determination of the enzyme concentration
        in solution e.g., the Bradford method,
        Lowry method, UV absorption, activity
        assays, ELISA, etc.""",
    )
    activity: float = Field(
        default=...,
        description="""The activity of the biocatalyst can be expressed
        either as volumetric activity, which
        considers the total activity of the
        enzyme in the solution, or as specific
        activity, which takes into account the
        enzyme's purity and indicates the activity
        of an enzyme per unit of enzyme protein
        or enzyme mass. If the biocatalyst has
        been purchased, it is advisable to look
        up more precise information (e.g. via an
        SOP) regarding the activities specified
        by the manufacturer, as these may differ
        from the values determined by yourself
        (different activity assays can lead to
        different activity values). In addition,
        the loss of activity of the biocatalyst
        over the storage period should be taken
        into account.""",
    )
    activity_unit: str = Field(
        default=...,
        description="""The enzyme's activity can be expressed either
        as specific activity[] U/mg (Units per
        milligram) or as volumetric activity[] U/
        mL (Units per milliliter) or as kcat[]
        time-1 (catalytic const. or turnover
        number).""",
    )
    activity_determination_method: str = Field(
        default=...,
        description="""Enzyme activity can be measured in various
        ways, including spectrophotometrically,
        colorimetrically, fluorometrically, assays
        and using biosensors, etc.""",
    )
    formulation: str = Field(
        default=...,
        description="""Depending on the formulation, the biocatalyst can
        be applied dissolved in a solvent or as
        a dried powder. It defines the physical
        state in which the biocatalyst is applied
        in the reaction.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:PurifiedBiocatalyst/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:PurifiedBiocatalyst",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class CrudeCellExtract(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    cell_disruption_process: str = Field(
        default=...,
        description="""Cell disruption processes and methods
        include various techniques such as
        mechanical disruption (e.g., grinding,
        homogenization, ultrasonication, french
        press), chemical disruption (e.g.,
        detergents, enzymes), physical techniques
        (e.g., electroporation, high-pressure
        homogenization, thermal treatment)
        to break cell walls and release cell
        contents.""",
    )
    concentration: float = Field(
        default=...,
        description="""Concentration of the biocatalyst.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""Concentration of the biocatalyst is typically
        expressed in g/L (grams per liter).""",
    )
    concentration_determination_method: str = Field(
        default=...,
        description="""It is important to specify the type of
        concentration determination. There are
        numerous methods available to determine
        protein content, yet only a few are
        suitable for estimating or determining
        the protein content of the target protein
        within a mixture. Some of these methods
        include activity assays or the Western
        blotting technique, which relies on
        prior SDS-PAGE and antibody binding for
        detection.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:CrudeCellExtract/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:CrudeCellExtract",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class WholeCellBiocatalyst(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    harvesting_method: str = Field(
        default=...,
        description="""In biotechnological processes, there are various
        methods for harvesting cells, including
        centrifugation, filtration, precipitation,
        etc.""",
    )
    concentration: float = Field(
        default=...,
        description="""In the case of whole-cell catalysts, the cell
        concentration or cell mass is commonly
        used as a measure.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""In case of lyophilized cells, the quantity of
        lyophilized cells can be specified in
        g (grams) or kg (kilograms). If wet
        cells are used, the cell concentration
        can be indicated in cells/mL (cells per
        milliliter) or cells/g (cells per gram) of
        wet cell weight. Other common indications
        of the concentration of wet cells as
        biocatalysts are the cell concentration
        in g/L (grams per liter) or OD (optical
        density).""",
    )
    concentration_determination_method: str = Field(
        default=...,
        description="""Specify the method for cell number per cell weight
        determination (e.g., flow cytometry,
        weight of dry biomass, spectrophotometry).""",
    )
    formulation: str = Field(
        default=...,
        description="""When applying a whole cell biocatalyst, there are
        various options. Cultivated cells can be
        lyophilized or used as wet cells after
        separation from the medium.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:WholeCellBiocatalyst/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:WholeCellBiocatalyst",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SecretedEnzyme(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    separation_method: str = Field(
        default=...,
        description="""There are various methods to separate the
        supernatant from the cells, common methods
        include centrifugation, filtration,
        sedimentation, etc.""",
    )
    concentration: float = Field(
        default=...,
        description="""Concentration of the biocatalyst.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""Concentration of the biocatalyst is typically
        expressed in g/L (grams per liter).""",
    )
    concentration_determination_method: str = Field(
        default=...,
        description="""It is important to specify the type of
        concentration determination. There are
        numerous methods available to determine
        protein content, yet only a few are
        suitable for estimating or determining
        the protein content of the target protein
        within a mixture. Some of these methods
        include activity assays or the Western
        blotting technique, which relies on
        prior SDS-PAGE and antibody binding for
        detection.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:SecretedEnzyme/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:SecretedEnzyme",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class CellFreeProduction(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    source_of_cellfree_extract: str = Field(
        default=...,
        description="""Specifiy the organism or cell type from which the
        cell-free extract is derived (e.g., by
        describing the genus and species). These
        could be bacterial, plant, animal, or
        another sources. If available, reference
        can be made to an appropriate database
        entry.""",
    )
    concentration: float = Field(
        default=...,
        description="""Concentration of the biocatalyst.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""Concentration of the biocatalyst is typically
        expressed in g/L (grams per liter).""",
    )
    concentration_determination_method: str = Field(
        default=...,
        description="""It is important to specify the type of
        concentration determination. There are
        numerous methods available to determine
        protein content, yet only a few are
        suitable for estimating or determining
        the protein content of the target protein
        within a mixture. Some of these methods
        include activity assays or the Western
        blotting technique, which relies on
        prior SDS-PAGE and antibody binding for
        detection.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:CellFreeProduction/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:CellFreeProduction",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Immobilised(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    biocatalyst: str = Field(
        default=...,
        description="""When it comes to the immobilization method, it
        is also important to mention how the
        biocatalyst to be immobilized is present
        (for example, as a purified enzyme, or as
        a crude cell extract, etc.).""",
    )
    immobilisation_chemistry: str = Field(
        default=...,
        description="""This aspect denotes the specific chemical
        methods or techniques used to attach the
        enzymes onto the chosen base material.
        Different immobilization chemistries
        involve various covalent or non-
        covalent bonding strategies, including
        crosslinking, adsorption, covalent
        bonding, encapsulation, specific binding
        via (affinity)tag, or entrapment.""",
    )
    carrier_material: str = Field(
        default=...,
        description="""If a support material, base, or carrier was
        utilized, it is necessary to specify the
        material's name (e.g., gel, membrane,
        particle) along with the supplier and
        further product details ( if_applicable )""",
    )
    linkers: str = Field(
        default=...,
        description="""Linkers are chemical compounds used to establish
        a connection or bridge between the enzymes
        and the carrier material. These linkers
        play a vital role in stabilizing the
        immobilized enzymes and can influence
        the efficiency and functionality of the
        immobilization process. They facilitate
        binding between the enzymes and the
        carrier material, promoting a stable and
        active biocatalyst structure. Common and
        widespread linkers are spacer molecules,
        crosslinkers, avidin-biotin or silane
        coupling agents. ( if_applicable )""",
    )
    immobilisation_method: str = Field(
        default=...,
        description="""Specify further details regarding the
        immobilisation method of the enzyme. For a
        comprehensive report around the technical
        key data of the immobilization process
        or method, see literature for further
        information, e.g. Ansorge-Schumacher2.""",
    )
    purification_method: str = Field(
        default=...,
        description="""The purification methods can vary depending
        on whether it involves whole cells
        or free enzymes. In the case of whole
        cells, methods such as centrifugation,
        filtration, or flow cytometry can be
        employed. In the case of free enzymes,
        methods like cell lysis, filtration,
        chromatography, and precipitation, among
        others, may be used.""",
    )
    concentration: float = Field(
        default=...,
        description="""Concentration of the biocatalyst or the whole
        cells on the immobilised phase.""",
    )
    concentration_unit: str = Field(
        default=...,
        description="""For immobilized enzymes, the concentration is
        often quantified in terms of enzyme
        activity per volume (e.g., units per
        milliliter, U/mL) or weight measurements
        such as milligrams or grams per liter (mg/
        L or g/L). When referring to immobilized
        cells (not the enzymes themselves), units
        of cells/mL (cells per milliliter) or
        cells/g (cells per gram) are commonly
        utilized.""",
    )
    concentration_determination_method: str = Field(
        default=...,
        description="""Various methods are available to determine the
        concentration of immobilized enzymes or
        cells. For immobilized enzymes, methods
        such as protein measurement or enzymatic
        activity assays can be used. The protein
        determination can be determined on the
        carrier material using a BCA test or
        as a differential measurement using the
        Bradford method, $\Delta$280 or also
        after detachment of the enzyme from the
        carrier material. An activity measurement
        is best suited as it provides the activity
        per gram of immobilized material. For
        immobilized cells, methods like flow
        cytometry or biomass measurement are
        applicable.""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific methods,
        procedures, characteristics or aspects
        related to the biocatalyst that are
        important for reproducibility and are not
        described by the aforementioned metadata,
        they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:Immobilised/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:Immobilised",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class StorageConditions(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
    )  # type: ignore

    temperature: float = Field(
        default=...,
        description="""The temperature at which the reactant is stored.""",
    )
    temperature_unit: str = Field(
        default=...,
        description="""The temperature can be specified in units such as
        K, °C, or °F.""",
    )
    storage_start: date = Field(
        default=...,
        description="""The date since the biocatalyst has been stored.""",
    )
    additives: str = Field(
        default=...,
        description="""Additives for the storage of biocatalyst can
        include antioxidants, stabilizers,
        drying agent, or even inert gases (argon,
        nitrogen), among others.""",
    )
    drying_method: str = Field(
        default=...,
        description="""For biocatalysts, various drying methods are
        employed (e.g., freeze-drying, also
        known as lyophilization, spray-drying,
        a method that involves atomizing a
        solution into small particles before
        drying, or vacuum drying, which removes
        moisture through low-pressure conditions).
        ( if_applicable )""",
    )
    special_treatment: str = Field(
        default=...,
        description="""If there are any other specific characteristics
        or aspects related to the biocatalyst
        that are important for reproducibility and
        are not described by the aforementioned
        metadata, they should be explained here.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "stbc:StorageConditions/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory=lambda: [
            "stbc:StorageConditions",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


# Rebuild all the classes within this file
for cls in [
    BiocatalystPurchased,
    BiocatalystSelfProduced,
    PurifiedBiocatalyst,
    CrudeCellExtract,
    WholeCellBiocatalyst,
    SecretedEnzyme,
    CellFreeProduction,
    Immobilised,
    StorageConditions,
]:
    cls.model_rebuild()
