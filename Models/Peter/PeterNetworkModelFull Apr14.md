
# Peter Halling network data model for applied biocatalysis 

The aim of this model structure is to show how attributes can be grouped to minimise repetition - so that each attribute appears only once whenever possible. Thus details about description, requirements, validation etc can be specified (and subsequently coded) just in one place for each group of attributes. This draft is obviously based on the data model we have worked on extensively and published, and now contains most of the attributes in that published model - I have omitted some on topics I am not particularly familiar with, so don't have confidence in proposing how the attributes might be grouped. There are comments in the descriptions in many places where there is clearly scope to extend and improve the model. I should acknowledge that others in the working group have contributed useful ideas and comments in the development of this structure, and I'm sure more views will inform future development.

Many of the attributes collect values of a quantity with units. The published model uses separate attributes for the numerical value and the units (as a string). But I think we recognise that it is better to define a Type that links the number and the units, and we need to work out the best way to do this. In the current draft, for the time being I have just used a single attribute with Type float. This is essentially a placeholder until we have decided the best general solution.

### BiocatalysisReactionSet

Collects a set of biocatalysis reactions carried out as (part of) a study. Each will be essentially a batch or fed-batch reaction, perhaps with continuous gas supply. Typically most of the conditions will be similar for all the reactions in the set, but there will be some differences in one or more attributes, e.g. temperature, pH, type of biocatalyst, starting materials used, concentrations in the reaction mixture. Some reactions will probably be replicates. Results from the whole set may be summarised by fitted values, for example kinetic parameters.

- Reactions
  - Type: BiocatalysisReaction
  - description: Details of one reaction
  - Multiple: True
- ModelFitting
  - Type: ModelFitting
  - description: Details of how data from the set of reactions has been fitted to a model, and the parameters obtained from the fit (e.g. Km, V)
  - Multiple: True
- OtherAnalysis
  - Type: string
  - description: Details of other analysis (other than model fitting) applied to (part of) the whole set. For example might include graphs presenting dependencies on varied conditions.


### ModelFitting
Describes the procedure and results of fitting a model to data on biocatalytic reactions

- EquationUsed
  - Type: string
  - description: The equation to which data has been fitted, e.g. Michaelis-Menten, more complex kinetic equations, Arrhenius. Better should become an equation type in some commonly used system.
- FittingDetails
  - Type: string
  - description: Information about the fitting process, e.g. data selection, data error estimates, fitting criteria, algorithm used
- ParameterFitted
  - Type: string
  - description: The identity of a parameter. Better to have compound type that links to equation that contains this parameter
  - Multiple: True
- FittedValue
  - Type: float
  - description: The best fit value of a parameter. Better to have compound type that links to equation that contains this parameter, the parameter identity, the value and the fitting error
  - Multiple: True
- FittedValueError
  - Type: float
  - description: The error estimate for the parameter value, obtained from the fitting process. Better to have compound type that links to equation that contains this parameter, the parameter identity, the value and the fitting error
  - Multiple: True


### BiocatalysisReaction

Collects details of one reaction, essentially a batch or fed-batch, perhaps with continuous gas supply. 

- Conditions
  - Type: BatchIncubation
  - description: Details of conditions for this reaction
- ExpectedReactions
  - Type: string
  - description: One or more reactions expected to occur under the conditions used, each shown as a (bio)chemical equation
- WhatIsMeasured
  - Type: MeasuredSpecies
  - description: Identifies the species measured to monitor the progress of the reaction, and some information about the methods applied to do so. If more than one species are measured, they should be assigned identifiers so they can be referred to in time point data. In the case of chiral materials, probably want to allow recording of total concentration and enantiomeric excess, instead of just two concentrations.
  - Multiple: True
- SampleVolume
  - Type: float
  - description: The volume of each sample removed for analysis. Could be an absolute value, or as a fraction of the total volume of the reaction mixture. Can be important when a significant fraction of the reaction mixture is removed in samples, but not all phases are removed together - for example biocatalyst concentration increases because it is not removed in the samples.
- ProgressData
  - Type: TimePoint
  - description: One or more data points showing the reaction progress, i.e. time values and corresponding concentrations of measured species
  - Multiple: True
- InitialRate
  - Type: float
  - description: An estimate of initial rate. If the reaction is monitored continuously (e.g. by spectrophotometry) the initial rate will be extracted fairly directly. In cases of discontinuous data, initial rate might be estimated by analysis of a series of progress data points. Could expand this to a separate Object, including details of method used to estimate initial rate – but probably this goes beyond what would normally be considered necessary. 

### MeasuredSpecies
Collects the identity of a species measured in order to monitor the reaction, together with some information on the analytical method used

- TheSpecies
  - Type: SmallCompound, Macromolecule
  - description: The identity of the species measured
- MeasurementMethod
  - Type: string
  - description: The method used to measure its concentration, e.g. spectrophotometry, HPLC, GC, NMR. Better change this to an enumerated list.
- MethodDetails
  - Type: string
  - description: Any necessary details of how the method is applied, including standardisation

### TimePoint
Results of analysis at a single time point during a reaction

- ReactionTime
  - Type: float
  - description: The elapsed time from the start of the reaction
- MeasuredConcentrations
  - Type: float
  - description: The concentration(s) measured at that time point. If more than one species are measured during the reaction, need to use identifiers so each concentration is linked to correct species. Need to allow for possibility that at each time point not every species may be measured.
  - Multiple: True


### BatchIncubation

Describes an operation in which a mixture is prepared and then held under defined conditions for a period of time, during which a reaction or similar process may occur. This might be a biocatalytic reaction, but can also be a step in chemical modification, immobilisation or some other process as part of biocatalyst preparation. Hence this is an Object much referred to elsewhere. Fed-batch operation is currently included under this Object, but could also be separated as a different Object. Continuous supply of a gas (e.g. by sparging) is also included, if the process is otherwise run as a batch or fed-batch.
Many of the attributes are only usually expected under particular circumstances: GasSupply only if this is used; FedBatchDetails only if operated as a fed-batch; MixingConditions only where the medium is a MultiPhaseDispersion or a fed-batch is used; BatchTime is not expected for a biocatalytic reaction; DispersionSampling only when the medium is a MultiPhaseDispersion; SampleQuenching only when the samples may contain active biocatalyst, so the reaction must be stopped before analysis.

- Temperature
  - Type: float
  - description: The temperature held during the incubation. At present taken to be constant - coverage of programmed T to be dealt with later
- Pressure
  - Type: float
  - description: The pressure applied during the incubation - only required if not atmospheric
- TheMedium
  - Type: Solution, MultiPhaseDispersion
  - description: What is being incubated, a solution or a multi-phase dispersion
- GasSupply
  - Type: GasSupplyDetails
  - description: Details of a gas being supplied continuously to the reaction mixture, usually by sparging, if this is done
- FedBatchDetails
  - Type: pHmeasureAdjust, ConcentrationControl, ProgrammedFeed
  - description: If this is a fed-batch, information on the details. To cover three categories: 1) Control of pH; 2) Feeding in an attempt to control other concentrations based on measurements during reaction, like remaining reactant concentration; 3) Feeding according to a pre-set schedule, either continuous slow feed or time-programmed dosing. Sometimes pH may be controlled to a time dependent profile of values, rather than a single fixed value - this would require an extension to the data model.
  - Multiple: True
- MixingConditions
  - Type: ShakenVessel, StirredReactor, FlowImpelledReactor
  - description: Description of features affecting mixing during the incubation (vessel, agitation etc). Normally only required when a multi-phase dispersion is incubated, or when additions are made in fed-batch mode. The type of vessel is closely linked to the way its contents are agitated. So a vial, a well-plate or a simple flask can only be agitated by some form of shaking. Anything with a mechanical stirrer will be classified as a stirred reactor - this can range from a large vial or beaker with a magnetic flea inside to a highly engineered reactor with multiple ports and sensors. A third possibility is a reactor mixed by gas or liquid pumping.
- BatchTime
  - Type: float
  - description: The time for which the batch is incubated. Not normally needed when this is a monitored biocatalytic reaction, as times will be implicit in the results. But required where the incubation is a step in biocatalyst preparation or modification.
- DispersionSampling
  - Type: RepresentativeSample, OnePhaseSample
  - description: Details of sampling procedures when the medium is a MultiPhaseDispersion. Options are to attempt to obtain a representative sample of the whole mixture, or to separate phases and take a sample of just one. (Sampling multiple separated phases is possible but unusual, possible future extension).  
- SampleQuenching
  - Type: StopReagent, TemperatureChange
  - description: Methods used to stop the reaction before analysis, when the samples will still contain active biocatalyst. At present covers rapid mixing with a solution that acts as a stop reagent, or use of temperature (heat treatment, or cooling). Other options may be added later.


### MultiPhaseDispersion

Description of a mixture with more than one phase, which might may include liquids, solids or gases. This might be a reaction mixture, or something used in another operation, e.g. as part of an immobilisation protocol. The order in which items were added can be important, so should be recorded unless it is known to have no effect - not sure how to encode this formally in the data model. Measurement or adjustment of pH needs to be recorded at the correct position in the sequence of making up the mixture, which might not be at the end.

- AddedItem
  - Type: AddedItemwithAmount
  - description: Details of a liquid, biocatalyst or solid item added to the mix.
  - Multiple: True
- pHmeasuredAdjusted
  - Type: pHmeasureAdjust
  - description: A measurement of pH in the solution or an adjustment to a target value - as noted, need to specify at what stage in making up the mixture the pH was measured

### AddedItemwithAmount

Description of one item added in making up a multi-phase mixture (where not everything dissolves to make a homogeneous solution). 

- AnItem
  - Type: Solution, BiocatalystUsed, DescribeSolid
  - description: Details of an item added to the mix. The possibilities covered at present are: 1) A solution or a neat liquid; 2) a soluble enzyme or biocatalyst; 3) a solid biocatalyst; 4) a solid item other than a biocatalyst
- AmountAdded
  - Type: float
  - description: The amount of the item added. This might be given as an absolute amount or volume, e.g. g or L. It might also be given relative to one other defined item in the mixture, e.g. g per L liquid, L per g biocatalyst. The same basis for amount added needs to be used for all items added to the same mixture.


### Solution

Description of a liquid or solution. A single liquid phase, usually containing dissolved solutes. This might be a reaction mixture, an item added in preparing a multi-phase reaction mixture, or something used in another operation, e.g. as part of a modification or immobilisation protocol. Measurement or adjustment of pH (if used) needs to be recorded as at a defined stage of making up the solution, which might not be at the end when all solutes have been added. (An alternative way to record this would have two different attributes, ASoluteAddedBeforepH and ASoluteAddedAfterpH. But in general we need a system to record the sequence in which events occur here, and in many other sections.)

- MainSolvent
  - Type: SmallCompound
  - description: Details of the (predominant) solvent. (If two are in equal amounts, choose either and enter the other as a dissolved compound.)
- ASolute
  - Type: SolutewithConc
  - description: Details of one solute (a small molecule, a biocatalyst or another macromolecule) added to the solution
  - Multiple: True
- pHdetails
  - Type: pHmeasureAdjust
  - description: A measurement of pH in the solution, or an adjustment with acid or alkali to a target value - as noted, need to specify what was present at the stage this was done.


### SmallCompound

Defines a small molecule or salt used as part of a recipe. At least one of the identifiers is required to avoid ambiguity. Source and purity are only required where it is believed they may have significant effects.

- CompoundName
  - Type: string
  - description: usual name of the substance, e.g. as obtained from PubChem
- IUPAC
  - Type: string
  - description: IUPAC name
- Smiles
  - Type: string
  - Description: SMILES (Simplified Molecular Input Line Entry System) is a chemical notation used to represent and describe molecular structures in a simplified and human-readable format.
- InChi
  - Type: string
  - description: InChi string
- ChEBI\_ID
  - Type: string
  - description: identifier in ChEBI database
- PubChem\_CID
  - Type: string
  - description: identifier in PubChem database
- Source
  - Type: SuppliedProduct, SelfProducedMaterial
  - description: source of compound, either from supplier or made in-house. Not needed for common commercial chemicals unless thought significant
- Purity
  - Type: string
  - description: typically expressed in percentage (%) of the pure desired compound relative to the total mass or volume of the material used


### SolutewithConc

Defines the identity and concentration of an item dissolved in a solution. 

- TheMaterial
  - Type: SmallCompound, BiocatalystUsed, Macromolecule
  - description: Details of the material added: a small molecule or salt solute; an enzyme or biocatalyst that will dissolve completely; or a non-enzyme macromolecular component
- Concentration
  - Type: float
  - description: concentration of the substance. This requires units e.g. M, g/L, %v. For the biocatalyst the units could be based on activity assayed in a defined reaction, so e.g. U/L.


### pHmeasureAdjust

Report a pH measurement, on a solution or multi-phase mixture, normally using a glass electrode. To include adjustment of pH to a desired value, either once during preparation, or continuously during a reaction. Some attributes will only be required in particular circumstances: NonaqueousCalibration only in the unusual case when calibration is not done with dilute aqueous standard buffers; Titrant only when this is added to adjust/control pH; ControlSystem only when continuous pH control is applied.

- pHvalue
  - Type: float
  - description: the directly measured value, which may be a targeted value after adjustment or during control (The value should not be adjusted, e.g. to different temperature, although this could be reported in text notes).
- MeasurementTemperature
  - Type: float
  - description: temperature of the solution or mixture when measured
- CalibrationTemperature
  - Type: float
  - description: temperature at which the electrode was calibrated
- NonaqueousCalibration
  - Type: string
  - description: report the calibration medium where this is not dilute aqueous (e.g. aqueous-organic mixture) and the nature of the set buffers used
- Titrant
  - Type: Solution
  - description: the acid or alkali used to adjust pH where this occurs
- ControlSystem
  - Type: string
  - description: When pH is continually controlled, details of the control algorithm and equipment used, perhaps with the achieved range of pH around the set point


### Macromolecule

Describes a macromolecular compound (other than an enzyme) used in an experiment. This Object still needs work to give comprehensive coverage, probably with introduction of sub-tables.

- CompoundName
  - Type: string
  - description: accepted name for the material, ideally as used in an authoritative database
- DatabaseUsed
  - Type: string
  - description: name of a database that gives further details on the material
- Identifier
  - Type: string
  - description: identifier in this database
- Source
  - Type: SuppliedProduct, SelfProducedMaterial
  - description: source of compound, either from an external supplier, or produced in house
- Purity
  - Type: string
  - description: information appropriate to the class of compound used

### SelfProducedMaterial

Details of the preparation in-house of a material (other than a biocatalyst) used in the experiments
- ProductionMethod
  - Type: string
  - description: Details of the protocol, perhaps a literature reference. Might become a more structured table later

### DescribeSolid
Details of a solid phase, other than a biocatalyst, added in making a multi-phase dispersion. Needs expansion to a fuller table, at present just a place-holder
- Details
  - Type: string
  - description: some information


### GasSupplyDetails
Details of a gas being supplied continuously to the reaction mixture, usually by sparging

- Composition
  - Type: string
  - description: The composition of the gas stream. "Air" is acceptable, otherwise give mole/volume fractions of each gas present, e.g. 100% O2, 20% CO2 plus 80% air.
- FlowRate
  - Type: float
  - description: Best given as volume per volume reaction mixture per unit time
- ContactSystem
  - Type: string
  - description: More or less a placeholder, will later require details of reactor, e.g. sparger type, location relative to impeller



### ConcentrationControl
Fed-batch in which measurements during the reaction are used to decide feed schedule

- MonitoredSpecies
  - Type: MeasuredSpecies
  - description: the species whose concentration is measured in order to choose feed schedule. It is possible that more than one species may be measured to provide basis for feeding - might need extension to cover this
- FeedAlgorithm
  - Type: string
  - description: how the amount or rate of feed is calculated based on the concentration measured. Should probably be extended to a sub-table that obtains more structured information
- FeedMade
  - Type: Solution, MultiPhaseDispersion, DescribeSolid
  - description: The composition of the feed entering the batch. At present restricted to one type of feed.


### ProgrammedFeed
Details of feed to a batch programmed in advance of run. Only one of ContinuousFeedRate or DosingSchedule is expected.

- FeedMade
  - Type: Solution, MultiPhaseDispersion, DescribeSolid
  - description: The composition of the feed entering the batch. At present restricted to one type of feed.
- ContinuousFeedRate
  - Type: float
  - description: The flow rate of the feed, normally as a ratio to the volume of the reaction mixture, e.g. 0.001 volume per volume per hour
- DosingSchedule
  - Type: string
  - description: Details of when and how much feed is added, e.g. 0.01 volume per volume every 3 hours. Should become a more structured table. 


### ShakenVessel
Reports details of a vial, a well-plate or a simple flask agitated by some form of shaking. Multi-well plates are commonly used in high throughput experiments. Effectively these consist of an array of identical vials in which individual reactions occur. So the conditions for any one reaction are based on the properties of a single well.

- Vessel
  - Type: VesselDescription
  - description: Details of the vessel that is shaken
- ShakingType
  - Type: string
  - description: The type of shaking used to mix the reaction (e.g., horizontal reciprocal, vertical reciprocal, horizontal rotary, vertical (end-over-end) rotary).
- Deflection
  - Type: float
  - Description: Information about the extent of deflection in the shaking movement - length of reciprocal motion, diameter of rotatory motion.
- Speed
  - Type: float
  - Description: Specify the speed or frequency at which the shaking was conducted, i.e. strokes or revolutions per unit time.
- VesselOrientation
  - Type: string
  - Description: Information regarding the orientation of the vessel in the shaking system relative to deflection. Most commonly the long axis of the vessel will be vertical, but it may be mounted horizontally or at an angle for better agitation of contents. 

### VesselDescription

Describes basic features of a vessel that may be used to contain a reaction mixture. It covers attributes that should be identifiable for a whole range of vessels, from small vials and wells on a plate, to large tanks.

- HeightInternal
  - Type: float
  - description: The height of the inside of the vessel, where the reaction mixture will be held. Should extend right to the top or lid, including any headspace.
- DiameterInternal
  - Type: float
  - description: The diameter of the inside of the vessel, where the reaction mixture will be held.
- Shape
  - Type: string
  - description: Information about the shape of the inside of the vessel. Probably better cover most common cases as an enumerated list: cylindrical, conical, square prism. Bottom might be: flat or round.
- Sealing
  - Type: string
  - description: details of any sealing at the top of the vessel. Might be open to the air, or covered with a cap, stopper, head-plate etc. If the vessel is operated such that the reaction mixture contacts the seal (e.g. when the vessel is shaken), then the material of the seal should be declared among ContactMaterial below.
- Capacity
  - Type: float
  - description: The volume contained when filled to the top
- VolumeFilled
  - Type: float
  - description: The volume of the reaction mixture contained. Might be given as a fraction of capacity.
- ContactMaterial
  - Type: string
  - description: Identify the material(s) in contact with the reaction mixture, in cases where this might be significant. e.g. glass, polypropylene, stainless steel. In the case of plastics, manufacturers may not declare the precise chemical nature, so the brand name and product code or similar should be reported.


### StirredReactor
Reports details of a vessel with a mechanical stirrer - this can range from a large vial or beaker with a magnetic flea inside to a highly engineered reactor with multiple ports and sensors. 

- Vessel
  - Type: VesselDescription
  - description: Details of the vessel walls and head-plate.
- Baffles
  - Type: string
  - description: Details of any baffles or similar placed around the walls of the vessel
- ImpellerType
  - Type: MagneticFollower, ShaftImpellers
  - description: Two main classes of impeller with different key characteristics.
- RotationRate
  - Type: float
  - Description: Specify the speed or frequency at which the impeller rotates.
- PowerPerVolume
  - Type: float
  - Description: The amount of stirring power input into a system per unit volume of the reaction mixture.


### MagneticFollower
Collects details of a magnetic stirrer bar used

- StirBarShape
  - Type: string
  - description: The shape of the magnetic stirrer bar. Should perhaps become an enumerated list: cylindrical horizontal axis (most common), oval, octagonal, cylindrical vertical axis with blades. Different shapes can interact with the reaction mixture differently, influencing mixing patterns and efficiency.
- StirBarLength
  - Type: float
  - description: The longest horizontal dimension of the stirrer bar
- StirBarWidth
  - Type: float
  - description: A second dimension of the stirrer bar, such as the diameter of a cylindrical one
- ContactMaterial
  - Type: string
  - description: The surface materials of the stirrer bar in contact with the reaction mixture, e.g. PTFE, glass, stainless steel

### ShaftImpellers
Collects details of a stirring system attached to a rotating shaft

- ImpellerDiameter
  - Type: float
  - description: Diameter of the entire impeller between the tips of blades or similar
- ImpellerGeometry
  - Type: string
  - Description: There are various morphologies or geometries, such as radial impellers, axial impellers, helical ribbon impellers, paddle impellers, and more, depending on its design and intended purpose.
- NumberBlades
  - Type: float
  - Description: The number of blades on each impeller, often 2 or 4.
- BladeDimensions
  - Type: string
  - Description: The dimensions of each impeller blade. Typically rectangular, so there will be two larger dimensions, with thickness also in cases where it might have an effect. Should perhaps become more structured with multiple attributes.
- BladePitch
  - Type: float
  - Description: The pitch angle at which the blades of an impeller are positioned relative to the plane of rotation. It's typically expressed in ° (degrees). Simple impellers often have 90 degrees, but angled blades give better circulation in entire reaction mixture.
- ImpellerHeight
  - Type: float
  - Description: The vertical distance between the bottom of the vessel or container and the lowest point of the (lowest) impeller.
- NumberImpellers
  - Type: float
  - Description: The number of impellers on the shaft that are immersed in the reaction mixture. Often just one, but multiple impellers may be used for more uniform mixing
- ImpellerSpacing
  - Type: float
  - Description: The height distance between the impellers when there are more than one on the shaft


### FlowImpelledReactor
A reactor mixed by a flow of gas or liquid pumped externally.

- Properties
  - Type: string
  - description: Just a placeholder, needs extension to fuller table and probably sub-tables. We have some attributes in the published data model, but I don't know enough about this class of reactors to be confident in incorporating them here.


### RepresentativeSample
Details of how a (hopefully) representative sample is obtained from a MultiPhaseDispersion.

- Procedure
  - Type: string
  - description: How this is achieved, usually by sampling while under vigorous mixing, and perhaps evidence that the sample really is representative. Mainly a placeholder, better extended to more structured table.


### OnePhaseSample
Details of how a sample of just one phase in a MultiPhaseDispersion is obtained

- PhaseSeparation
  - Type: Separation
  - description: Details of how the phases are separated, using type defined below (although needs more detail in its definition there). 
- PhaseSampled
  - Type: string
  - description: Which of the separated phases is sampled. Might become an enumerated list, e.g. supernatant liquid, organic phase, wet precipitate.


### StopReagent
Details of how the reaction is stopped by rapid mixing with a stop reagent

- TheReagent
  - Type: Solution
  - description: The composition of the stop reagent used
- StoptoSampleRatio
  - Type: float
  - description: The volume of stop reagent added, as a ratio to the sample volume. i.e. parts of stop reagent per 1 part sample, may be fractional

### TemperatureChange
Details of a treatment to stop reaction in samples before analysis

- TemperatureApplied
  - Type: float
  - description: the higher temperature applied to inactivate the biocatalyst, or the lower temperature to greatly reduce its activity
- HoldTime
  - Type: float
  - description: how long the heat treatment is applied for, or the maximum time held after cooling before analysis


### ContinuousReaction
Details of the operation and results of a continuous reactor. This still needs more extension.

- FeedComposition
  - Type: Solution
  - description: Details of the liquid fed continuously to the reactor
- FeedRate
  - Type: float
  - description: Flow rate of feed to the reactor. Could have units based on absolute volume, or as ratio to volume of reactor (i.e. “dilution rate”).
- ReactorType
  - Type: PackedBed, StirredReactor
  - description: The type of reactor: currently either CSTR or PackedBed. The CSTR is described with the same attributes as a stirred tank used in batch or fed-batch. Will later need expanded to include more possibilities, membrane reactors etc
- ExpectedReactions
  - Type: string
  - description: One or more reactions expected to occur under the conditions used, each shown as a (bio)chemical equation
- WhatIsMeasured
  - Type: MeasuredSpecies
  - description: Identifies the species measured to monitor the behaviour of the reactor. Assumed to be at outlet of reactor (or equivalently, for a fully mixed CSTR, in the reactor itself). Also gives some information about the methods applied to measure the concentrations. If more than one species are measured, should be assigned identifiers so can be referred to in time point data. In the case of chiral materials, probably want to allow recording of total concentration and enantiomeric excess, instead of just two concentrations.
  - Multiple: True
- PerformanceData
  - Type: TimePoint
  - description: One or more data points showing the performance of the reactor, i.e. time values and corresponding concentrations of measured species. Time would normally be that elapsed since reactor start-up.
  - Multiple: True

### PackedBed

Describes the details of a packed bed reactor. At present assumes the biocatalyst is present as a bed of solid particles. Should later also allow for biocatalyst immobilised on the inner walls of a thin tube. 

- Diameter
  - Type: float
  - description: diameter of the tube in which the bed is packed. At present assumed to be cylindrical.
- ContactMaterials
  - Type: string
  - description: Materials in contact with the reaction mixture in the reactor, e.g. glass, polypropylene, stainless steel.
- PackingMaterial
  - Type: BiocatalystUsed
  - description: Details of a solid biocatalyst packed in the reactor. Later might need to allow for mixed packing, e.g. mixed with inert solid
- PackingAmount
  - Type: float
  - description: The amount of material packed in the bed, typically as mass
- OtherInformation
  - Type: string
  - description: Further information about the reactor and its behaviour, e.g. residence time distribution


### ProteinDescription

Describe the chemical nature of a protein used as an enzyme, or present as one active component of a more complicated biocatalyst. In some cases (e.g. a commercial product) some of this information may be unknown - if so, it is better to give no information rather than enter guesses.

- ProteinName
  - Type: string
  - description: name of the protein, if possible as used by UniProtKB or other database. The name will usually have a generic part based on the catalyzed reaction, for example 'lipase', and also designate a specific type by naming a source organism and/or code, such as '_Bacillus amyloliquefaciens_ alpha-amylase A'.
- ProteinSequence
  - Type: string
  - description: amino acid sequence using one letter code
- UniProtKBlink
  - Type: string
  - description: identifier code if sequence in UniProtKB, or explain relationship to a UniProtKB sequence (e.g. an engineered mutant)
- MolecularWeight
  - Type: float
  - description: The molecular weight of the enzyme
- PostTranslationalModification
  - Type: DescribePTM
  - description: To be used to describe modifications made in the cell during expression. Chemical modifications made during biocatalyst preparation should be described as part of FormulationModification.
- EnzymeClassification
  - Type: string
  - description: EC number, and perhaps further information about reference reaction catalysed

### BiocatalystUsed

Describes a biocatalyst as introduced into the reaction mixture to catalyse a reaction. It might consist of a single BiocatalystPreparation, which has been obtained from an external source or produced in-house. But it might also be the result of processes to formulate, modify or immobilise one or more BiocatalystPreparation items. The BiocatalystUsed may dissolve completely in the reaction mixture, or it may be in form of solid particles that remain suspended. Options for the nature of the particles include: a) whole cells or fragments of them that contain active enzyme(s); b) the result of immobilisation; c) (part-)dried particles added to a non-aqueous medium.

- Preparations
  - Type: BiocatalystPreparation
  - description: Details of one or more that have been used in making the biocatalyst used in a reaction - or of one that is the biocatalyst used
  - Multiple: true
- ConcentrationBasis
  - Type: string
  - description: How the concentration of the biocatalyst in the reaction mixture is specified. This might be as weight of a defined preparation, in moles of active enzyme present, an assay or total protein content, or in terms of activity in some standard assay. Like many other text fields, this could be replaced by a more structured Object.
- FormulationModification
  - Type: FormulationModification
  - description: Collects details of any formulation, modification, immobilisation etc that takes place after the biocatalyst is obtained or produced
- StorageandStability
  - Type: StorageStability
  - description: Collects information about how the biocatalyst is stored before use, and information about its stability during storage
- IsSoluble
  - Type: boolean
  - description: Will the biocatalyst dissolve in the reaction mixture
- SolidProperties
  - Type: string
  - description: If not soluble, information about the solid properties of the material used, e.g. particle size, wetting liquid content etc. Probably should later become a reference to a more structured sub-table in a separate Object.
- StandardAssay
  - Type: StandardAssay
  - description: Reports an assay of the catalytic activity of the biocatalyst in a standard reaction, used as part of its characterisation

### BiocatalystPreparation

Describes a biocatalyst preparation that has been obtained from an external source or produced in-house. If the ProteinDescription is fully completed, and Purity is good, then source details may strictly not be needed, although they may usefully be given.

- Protein
  - Type: ProteinDescription
  - description: Collects information about the active protein(s) in the preparation used
  - Multiple: true
- Source
  - Type: SuppliedProduct, SelfProduced
  - description: Links to one of the two possible source types, a commercial or similar external source, or details of how the biocatalyst has been produced in-house
- Purity
  - Type: ProteinPurity
  - description: Collects information about purity
- AmountBasis
  - Type: string
  - description: Information about how the amount of the biocatalyst is specified, e.g. mol of pure enzyme, mg of total protein, mg of dried preparation, units (specified) of enzyme activity in defined assay
- StorageandStability
  - Type: StorageStability
  - description: Collects information about how the biocatalyst is stored before use, and information about its stability during storage
- StandardAssay
  - Type: StandardAssay
  - description: Reports an assay of the catalytic activity of the biocatalyst in a standard reaction, used as part of its characterisation


### StandardAssay

Reports an assay of the catalytic activity of the biocatalyst in a standard reaction, used as part of its characterisation. Note this is not the target biocatalytic reaction, which should be reported via the separate Object for this. Rather this refers to measurements of activity in some reference reaction, often with model substrates, used to assess the properties of the biocatalyst.

- AssayConditions
  - Type: BatchIncubation
  - description: Reports the conditions for the standard assay
- MeasuredActivity
  - Type: string
  - description: More or less a placeholder at present, should become more detailed, perhaps a sub-table

### SuppliedProduct

Collect details where a biocatalyst or other material used is characterised by its provenance, usually from a commercial supplier

- Supplier
  - Type: string
  - description: Information about the supplier from which the material was obtained
- Name
  - Type: string
  - description: Name as given by the supplier
- ProductCode
  - Type: string
  - description: Reference code which identifies the product unambiguously among the range available from that supplier
- LotNo
  - Type: string
  - description: A lot or batch number for the material used

### SelfProduced

This section describes how a biocatalyst has been produced in the user's own lab. This will typically be by expression in cultured cells, but could also be via cell-free expression systems, or by extraction from bulk biomass.
I have retained attributes below that have been listed earlier by others, but I don't want to say too much about this topic because I don't have the necessary expertise. We should also note that most of the relevant methods here are common to other application areas in which proteins are expressed, and we might hope to build a consensus with experts from all these areas. We certainly need more details about the culture media, growth times, cell free expression medium etc. Also probably recovery, any purification. Some of these are probably best handled in sub-tables. An obvious way to structure this would be to have separate objects for: 1) Expression in cells; 2) Cell free expression; and 3) Extraction from biomass obtained elsewhere. But I'm not sure exactly how this structure would work best. Details on purification would be common to all three. Details of the DNA sequence would be common to 1 and 2. 

- ExpressionSystem
  - Type: string
  - description: description of expression system if heterologously expressed, including the organism which was used as heterologous expression system
- SequenceDNA
  - Type: string
  - description: The DNA sequence of the biocatalyst including any tags and linkers.
- SequencePlasmid
  - Type: string
  - description: The DNA sequence of the plasmid used to produce the biocatalyst. The sequence can be provided in plain text or as a database ID.
- SequenceSpecification
  - Type: string
  - description: All DNA sequence changes (e.g. codon optimization for E. coli, insertion of affinity tags, sequence truncation, etc.) should be provided.
- OriginOrganism
  - Type: string
  - description: The specific species or source from which the enzyme is derived or isolated, ideally with TaxonID
- Purification
  - Type: string
  - Description: The choice of purification methods is diverse and can impact the enzyme, with possible methods including chromatographic techniques, precipitation, HPLC, ultrafiltration, dialysis, salt fractionation,      etc.
- SpecialTreatment
  - Type: string
  - description: description of any further procedures or aspects relevant to the characterization of the protein and reproducibility of the generation of the protein


### ProteinPurity

- Purity
  - Type: float
  - description: Purity of enzymes typically expressed in percentage (%). It is usually stated as the percentage of the pure enzyme or active component relative to the total mass of the enzyme preparation.
- PurityDetermination
  - Type: string
  - description: Description of how the purity of the biocatalyst was determined. For purchased enzymes this might be a value quoted by the suppliers, but this might also be independently measured by the user.


### FormulationModification

This section deals with any treatment applied after the biocatalyst is purchased or produced, but before it is introduced to the reaction mixture. This includes chemical modification and immobilisation. There is often no completely unambiguous dividing line between the process of production and that of further modification.  In general, expression, extraction, purification and isolation would be considered part of production. But placing the dividing line in different places should not prevent the necessary metadata details being captured in one of the Objects.

The process of formulation or modification can generally be described as a sequence of steps that can be viewed as either incubations, separations or characterisations. Hence the metadata required is the description of these steps in the correct sequence. Each of them could appear more than once, normally with different details. The results of characterisation might be classed as data rather than metadata, so I'm not quite sure how best to record them. It is also conceivable that continuous process steps might be used, might need future provision for this.

- SummaryAim
  - Type: string
  - description: A summary of the aim of the formulation or modification process. This might include the chemical changes expected, such as protein groups expected to react, links expected to be formed.
- AnIncubation
  - Type: BatchIncubation
  - description: Details of one batch incubation step
  - Multiple: True
- ASeparation
  - Type: Separation
  - description: Details of one separation step
  - Multiple: True
- ACharacterisation
  - Type: Characterisation
  - description: Details of one characterisation step. At present just a placeholder if these end up being recorded here.
  - Multiple: True

### Separation

Describes an operation in which two or more parts of a mixture are separated from each other, usually following an incubation. Typically a solid material will be separated from a supernatant liquid. Separation operations are often part of a protocol for chemical modification or immobilisation. Often just one of the separated materials will be desired for further processing or use, and the other will be discarded, perhaps after analysis. Separation may also include a washing step, and the washings may be combined with the initial supernatant, or may be discarded. Solid-liquid separations will usually be via settling under gravity, centrifugation or filtration. In future, might also need to allow for liquid-liquid separation. At present this Object is just a placeholder.
- SeparationDetails
  - Type: string
  - description: The details. Should expand to structured table


### Characterisation

Describes a characterisation of a biocatalyst, either the final product or an intermediate stage in production or modification. At present just a placeholder, as not sure whether this should be classed as metadata or handled separately as data.
- AMeasurement
  - Type: string
  - description: Details of the measurement. Should later become a more structured table.


### DescribePTM

Collect details of post-translational modifications that take place during expression of the protein. Should become a more structured table.

- PTMDetails
  - Type: string
  - description: Details of Phosphorylation, Glycosylation, Acetylation, Hydroxylation, Methylation, Other. Should be extended into more detailed table with specific fields


### StorageStability

Details of how the biocatalyst was stored after preparation and before use (if it was not used immediately). Only one of WetUnfrozen, Frozen or Dried is expected.

- WetUnfrozen
  - Type: BatchIncubation
  - description: collect full details of medium, temperature etc
- Frozen
  - Type: FrozenStorage
  - description: details of frozen storage method
- Dried
  - Type: DryStorage
  - description: details of storage by drying
- MaximalStorageTime
  - Type: float
  - description: longest time of storage under the reported conditions before use
- StatementLoss
  - Type: string
  - description: Statement about observed loss of activity under the above conditions

### Freezing

Describes a process of freezing a sample. Might be a precursor to frozen storage, or freeze drying. 
- WhatisFrozen
  - Type: Solution, MultiPhaseDispersion
  - description: The solution or multi-phase mixture that is to be frozen
- FreezeTemperature
  - Type: float
  - description: The target temperature for the freezing process
- FreezingProcess
  - Type: string
  - description: Any relevant details of the freezing process, e.g. equipment, cooling rate

### FrozenStorage

Describes storage by freezing and holding at low temperature

- InitialFreezing
  - Type: Freezing
  - description: The process of initial freezing
- HoldTemperature
  - Type: float
  - description: The temperature maintained through the storage process, e.g. -20 or -80 oC
- ThawProcess
  - Type: string
  - description: Any relevant details of how the sample is thawed before use

### DryStorage

Describes storage by drying. Only one of FreezeDrying, AirDrying or SprayDrying is expected - so once these are coded as separate Objects, would have attribute DryingMethod with 3 possible types

- FreezeDrying
  - Type: string
  - description: Details of a freeze-drying process. Should become a structured table, using Freezing as a sub-table
- AirDrying
  - Type: string
  - description: Details of an air-drying process. Should also become a structured table.
- SprayDrying
  - Type: string
  - description: Details of a spray-drying process. Should also become a structured table.
- HoldTemperature
  - Type: float
  - description: Temperature at which the dry preparation was held
- Rehydration
  - Type: string
  - description: Any significant details of how the biocatalyst is re-hydrated before use





