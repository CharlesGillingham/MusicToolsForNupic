# -----------------------------------------------------------------------------
# Message types
# -----------------------------------------------------------------------------
# possible values for message.messageNumber
Message_NoteOff		    = 0x80
Message_NoteOn		    = 0x90
Message_NotePressure    = 0xA0
Message_ControlChange   = 0xB0  # Includes mode, global and RPN messages.
Message_ProgramChange   = 0xC0
Message_ChannelPressure	= 0xD0
Message_PitchWheel		= 0xE0
Message_System          = 0xF0  # Includes Meta messages (in files)

# -----------------------------------------------------------------------------
# Channel messages
# -----------------------------------------------------------------------------
# values for message.channel
Channel_Min   = 0
Channel_Max   = 15
Channel_Count = 16

# Some special channels
Channel_Percussion =  9

# -----------------------------------------------------------------------------
# Channel messages / Note Messages
# -----------------------------------------------------------------------------
# values for message.note
Note_Min = 0
Note_Max = 127
Note_Count = 128

Note_C0      = 12
Note_A440    = 57
Note_MiddleC = 60 # C4
Note_C7      = 96

# Values for message.percussionInstrument
PercussionInstrument_AcousticBassDrum =  35
PercussionInstrument_BassDrum1        =  36
PercussionInstrument_AcousticSnare    =  38
PercussionInstrument_ClosedHiHat      =  42
# ... etc; there are many more

# -----------------------------------------------------------------------------
# Channel messages / Control Message
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Channel messages / Control Message / ContinuousControllers
# -----------------------------------------------------------------------------
# values for message.controllerNumber

Controller_BankSelect       = 0
Controller_ModulationWheel  = 1
Controller_BreathControl    = 2
Controller_Undefined1       = 3
Controller_FootController   = 4
Controller_PortamentoTime   = 5 # See also 537 and 84
Controller_DataEntry        = 6 # When used withRPN this controls the last registered parameter.
Controller_ChannelVolume    = 7
Controller_Balance          = 8
Controller_Undefined2       = 9
Controller_Pan              = 10
Controller_Expression       = 11
Controller_Effect1          = 12
Controller_Effect2          = 13
Controller_Undefined3       = 14
Controller_Undefined4       = 15
Controller_GeneralPurpose1  = 16
Controller_GeneralPurpose2  = 17
Controller_GeneralPurpose3  = 18
Controller_GeneralPurpose4  = 19

# fine control
# These are numbered strictly in parallel with the main value.

Controller_FineBankSelect       = 32 # (MIDIController_BankSelect | 0x20)
Controller_FineModulationWheel  = 33 # (MIDIController_ModulationWheel | 0x20)
Controller_FineBreathControl    = 34 # etc.
Controller_FineUndefined1       = 35
Controller_FineFootController   = 36
Controller_FinePortamentoTime   = 37
Controller_FineDataEntry        = 38
Controller_FineChannelVolume    = 39
Controller_FineBalance          = 40
Controller_FineUndefined2       = 41
Controller_FinePan              = 42
Controller_FineExpression       = 43
Controller_FineEffect1          = 44
Controller_FineEffect2          = 45
Controller_FineUndefined3       = 46
Controller_FineUndefined4       = 47
Controller_FineGeneralPurpose1  = 48
Controller_FineGeneralPurpose2  = 49
Controller_FineGeneralPurpose3  = 50
Controller_FineGeneralPurpose4  = 51

# -----------------------------------------------------------------------------
# Channel messages / Control Message / Sound control
# -----------------------------------------------------------------------------
# Values for message.controllerNumber

# sound control
Controller_SoundVariation        = 70
Controller_SoundTimbre           = 71  # AKA "FilterResonance"
Controller_SoundReleaseTime      = 72
Controller_SoundAttackTime       = 73
Controller_SoundBrightness       = 74
Controller_SoundDecayTime        = 75  # Not sure if 75-79 are GM standard or if they are Apple-specific
Controller_SoundVibratoRate      = 76  # (they are from AUMIDIDefs.h)
Controller_SoundVibratoDepth     = 77
Controller_SoundVibratoDelay     = 78
Controller_SoundController79     = 79

# portamento control
Controller_PortamentoSource      = 84  # Value is "source note" WHAT DOES THAT MEAN??

# effects
Controller_ReverbSend            = 91  # AKA ReverbLevel
Controller_Tremolo               = 92
Controller_ChorusSend            = 93  # AKA ChorusLevel
Controller_Detune                = 94
Controller_Celeste               = 95

# general purpose (assume continuous)
Controller_GeneralPurpose5       = 80
Controller_GeneralPurpose6       = 81
Controller_GeneralPurpose7       = 82
Controller_GeneralPurpose8       = 83

# -----------------------------------------------------------------------------
# Channel messages / Control Message / BinaryControllers
# -----------------------------------------------------------------------------
# Values for message.controllerNumber

Controller_Sustain          = 64 # AKA "Hold1"
Controller_PortamentoOnOff  = 65 # (see also 37 and 84)
Controller_Sostenato        = 66
Controller_Soft             = 67
Controller_Legato           = 68
Controller_Hold2            = 69

# -----------------------------------------------------------------------------
# Channel messages / Control Message / Registered Parameters
# -----------------------------------------------------------------------------
# The "registered parameter" system allows up to 16384 more virtual controllers.

RPN_PitchBendSensitivity	= 0x0000
RPN_MasterFineTuning		= 0x0001
RPN_MasterCoarseTuning		= 0x0002
RPN_ModDepthRange           = 0x0005
# ... there are many many more ...

RPN_Null					= 0x3fff	#! 0x7f/0x7f (from AUMIDIDefs.h: may be Apple-specific)

# Values for message.controllerNumber (These controller numbers should not be needed to send messages normalRPNControllers. The constructors above combine four messages to set anRPN parameter. However this interface does not currently provide an interface to parse a set of messages and determine the current value of anRPN parameter.
Controller_RPN_DataEntry_MSB                = 6
Controller_RPN_DataEntry_LSB                = 38
Controller_RPN_DataButtonIncrement          = 96
Controller_RPN_DataButtonDecrement          = 97
Controller_RPN_NonRegisteredParameter_LSB   = 98
Controller_RPN_NonRegisteredParameter_MSB   = 99
Controller_RPN_RegisteredParameter_LSB      = 100
Controller_RPN_RegisteredParameter_MSB      = 101

# -----------------------------------------------------------------------------
# Channel messages / Control Message / Global Control
# -----------------------------------------------------------------------------
# message.controllerNumber

Controller_Mode_AllSoundOff         = 120
Controller_Mode_AllControllersOff   = 121
Controller_Mode_LocalKeyboardOff    = 122
Controller_Mode_AllNotesOff         = 123

# -----------------------------------------------------------------------------
# Channel messages / Control Message / Channel Mode
# -----------------------------------------------------------------------------
# message.controllerNumber

Controller_Mode_OmniModeOff	  = 124
Controller_Mode_OmniModeOn    = 125
Controller_Mode_MonoOperation = 126
Controller_Mode_PolyOperation = 127

# -----------------------------------------------------------------------------
# Channel messages / Control Message / Channel Mode
# -----------------------------------------------------------------------------
# message.controlValueType
# Classify a controller by the type of data it provide and the function it performs

ControllerType_Continuous = 0 # value = 0..127
ControllerType_Fine       = 1 # value = 0..127
ControllerType_Binary     = 2 # value = 0 or 127 representing True or False
ControllerType_RPN        = 3 # used to define moreControllers (see below)
ControllerType_Mode       = 4 # value is ignored
ControllerType_Undefined  = 5 # probably represents an error

def ControlType( controlNumber ):
    if (controlNumber <= 19): return ControllerType_Continuous  # coarse
    if (controlNumber <= 31): return ControllerType_Undefined
    if (controlNumber <= 51): return ControllerType_Continuous  # fine
    if (controlNumber <= 63): return ControllerType_Undefined
    if (controlNumber <= 69): return ControllerType_Binary
    if (controlNumber <= 83): return ControllerType_Continuous  # sound
    if (controlNumber <= 90): return ControllerType_Undefined
    if (controlNumber <= 95): return ControllerType_Continuous  # effects
    if (controlNumber <= 101): return ControllerType_RPN
    if (controlNumber <= 199): return ControllerType_Undefined
    if (controlNumber <= 127): return ControllerType_Mode
    return ControllerType_Undefined

# -----------------------------------------------------------------------------
# Channel messages / Program Change
# -----------------------------------------------------------------------------
# message.programNumber

ProgramNumber_AcousticGrandPiano	= 0
ProgramNumber_BrightAcousticPiano	= 1
ProgramNumber_ElectricGrandPiano	= 2
ProgramNumber_HonkyTonkPiano		= 3
ProgramNumber_ElectricPiano1		= 4
ProgramNumber_ElectricPiano2		= 5
ProgramNumber_Harpsichord           = 6
ProgramNumber_Clavinet              = 7

ProgramNumber_Celesta               = 8
ProgramNumber_Glockenspiel          = 9
ProgramNumber_MusicBox              = 10
ProgramNumber_Vibraphone            = 11
ProgramNumber_Marimba               = 12
ProgramNumber_Xylophone             = 13
ProgramNumber_TubularBells          = 14
ProgramNumber_Dulcimer              = 15

ProgramNumber_DrawbarOrgan          = 16
ProgramNumber_PercussiveOrgan		= 17
ProgramNumber_RockOrgan             = 18
ProgramNumber_ChurchOrgan           = 19
ProgramNumber_ReedOrgan             = 20
ProgramNumber_Accordion             = 21
ProgramNumber_Harmonica             = 22
ProgramNumber_TangoAccordion		= 23

ProgramNumber_AcousticGuitarNylon	= 24
ProgramNumber_AcousticGuitarSteel	= 25
ProgramNumber_ElectricGuitarJazz	= 26
ProgramNumber_ElectricGuitarClean   = 27
ProgramNumber_ElectricGuitarMuted   = 28
ProgramNumber_OverdrivenGuitar      = 29
ProgramNumber_DistortionGuitar      = 30
ProgramNumber_GuitarHarmonics       = 31

ProgramNumber_AcousticBass          = 32
ProgramNumber_ElectricBassFinger    = 33
ProgramNumber_ElectricBassPick      = 34
ProgramNumber_FretlessBass          = 35
ProgramNumber_SlapBass1             = 36
ProgramNumber_SlapBass2             = 37
ProgramNumber_SynthBass1            = 38
ProgramNumber_SynthBass2            = 39

ProgramNumber_Violin                = 40
ProgramNumber_Viola                 = 41
ProgramNumber_Cello                 = 42
ProgramNumber_Contrabass            = 43
ProgramNumber_TremoloStrings		= 44
ProgramNumber_PizzicatoStrings		= 45
ProgramNumber_OrchestralHarp		= 46
ProgramNumber_Timpani               = 47
ProgramNumber_StringEnsemble1		= 48
ProgramNumber_StringEnsemble2		= 49
ProgramNumber_SynthStrings1         = 50
ProgramNumber_SynthStrings2         = 51
ProgramNumber_ChoirAahs             = 52
ProgramNumber_VoiceOohs             = 53
ProgramNumber_SynthChoir            = 54
ProgramNumber_OrchestraHit          = 55

ProgramNumber_Trumpet               = 56
ProgramNumber_Trombone              = 57
ProgramNumber_Tuba                  = 58
ProgramNumber_MutedTrumpet          = 59
ProgramNumber_FrenchHorn            = 60
ProgramNumber_BrassSection          = 61
ProgramNumber_SynthBrass1           = 62
ProgramNumber_SynthBrass2           = 63

ProgramNumber_SopranoSax            = 64
ProgramNumber_AltoSax               = 65
ProgramNumber_TenorSax              = 66
ProgramNumber_BaritoneSax           = 67
ProgramNumber_Oboe                  = 68
ProgramNumber_EnglishHorn           = 69
ProgramNumber_Bassoon               = 70
ProgramNumber_Clarinet              = 71
ProgramNumber_Piccolo               = 72
ProgramNumber_Flute                 = 73
ProgramNumber_Recorder              = 74
ProgramNumber_PanFlute              = 75
ProgramNumber_BlownBottle           = 76
ProgramNumber_Shakuhachi            = 77
ProgramNumber_Whistle               = 78
ProgramNumber_Ocarina               = 79

ProgramNumber_Lead_1_Square         = 80
ProgramNumber_Lead_2_Sawtooth       = 81
ProgramNumber_Lead_3_Calliope       = 82
ProgramNumber_Lead_4_Chiff          = 83
ProgramNumber_Lead_5_Charang        = 84
ProgramNumber_Lead_6_Voice          = 85
ProgramNumber_Lead_7_Fifths         = 86
ProgramNumber_Lead_8_BassAndLead    = 87

ProgramNumber_Pad_1_Newage          = 88
ProgramNumber_Pad_2_Warm            = 89
ProgramNumber_Pad_3_Polysynth       = 90
ProgramNumber_Pad_4_Choir           = 91
ProgramNumber_Pad_5_Bowed           = 92
ProgramNumber_Pad_6_Metallic        = 93
ProgramNumber_Pad_7_Halo            = 94
ProgramNumber_Pad_8_Sweep           = 95

ProgramNumber_FX_1_Rain             = 96
ProgramNumber_FX_2_Soundtrack       = 97
ProgramNumber_FX_3_Crystal          = 98
ProgramNumber_FX_4_Atmosphere       = 99
ProgramNumber_FX_5_Brightness       = 100
ProgramNumber_FX_6_Goblins          = 101
ProgramNumber_FX_7_Echoes           = 102

ProgramNumber_FX_8_SciFi            = 103
ProgramNumber_Sitar                 = 104
ProgramNumber_Banjo                 = 105
ProgramNumber_Shamisen              = 106
ProgramNumber_Koto                  = 107
ProgramNumber_Kalimba               = 108
ProgramNumber_Bagpipe               = 109
ProgramNumber_Fiddle                = 110
ProgramNumber_Shanai                = 111

ProgramNumber_TinkleBell            = 112
ProgramNumber_Agogo                 = 113
ProgramNumber_SteelDrums            = 114
ProgramNumber_Woodblock             = 115
ProgramNumber_TaikoDrum             = 116
ProgramNumber_MelodicTom            = 117
ProgramNumber_SynthDrum             = 118
ProgramNumber_ReverseCymbal         = 119

ProgramNumber_GuitarFretNoise		= 120
ProgramNumber_BreathNoise           = 121
ProgramNumber_Seashore              = 122
ProgramNumber_BirdTweet             = 123
ProgramNumber_TelephoneRing         = 124
ProgramNumber_Helicopter            = 125
ProgramNumber_Applause              = 126
ProgramNumber_Gunshot               = 127

ProgramNumber_Count                 = 128
ProgramNumber_Max                   = 127

# -----------------------------------------------------------------------------
#  Constants: Channel messages / Pitch wheel
# -----------------------------------------------------------------------------
# See http:#home.roadrunner.com/~jgglatt/tech/midispec/wheel.htm

PitchWheel_Min  = 0x0000
PitchWheel_Zero = 0x2000
PitchWheel_Max  = 0x3FFF

# -----------------------------------------------------------------------------
#  Constants: System Messages
# -----------------------------------------------------------------------------
# Values for message.systemMessageType

# System common messages

SystemMsg_SystemExclusive      = 0xF0
SystemMsg_MIDITimeCodeQtrFrame = 0xF1
SystemMsg_SongPosition         = 0xF2
SystemMsg_SongSelection        = 0xF3
SystemMsg_4_Undefined          = 0xF4
SystemMsg_5_Undefined          = 0xF5
SystemMsg_TuneRequest          = 0xF6
SystemMsg_EndofSysEx           = 0xF7

# System real time message
# These have no data bytes.
# Note that these messages can not appear in a MIDIFILE
SystemMsg_TimingClock         = 0xF8
SystemMsg_10_Undefined        = 0xF9
SystemMsg_Start               = 0xFA
SystemMsg_Continue            = 0xFB
SystemMsg_Stop                = 0xFC
SystemMsg_13_Undefined        = 0xFD
SystemMsg_ActiveSensing       = 0xFE
SystemMsg_SystemReset         = 0xFF
SystemMsg_Meta                = 0xFF
# SysteMsg_Meta is equal to MIDISystemMsg_SystemReset but MIDISystemMsg_SystemReset appears only in live streams and this only appears in files.

# Some constants to help navigate the list
SystemMsg_First               = 0xF0
SystemMsg_FirstRealTime       = 0xF8
SystemMsg_Last                = 0xFF

# Returned by message.systemMessageType if this is not a system message
SystemMsg_None                = 0x0F

# -----------------------------------------------------------------------------
# System Messages /Meta Messages
# -----------------------------------------------------------------------------
# values for messages.metaMessageType

# (Based on
# http:#253.ccarh.org/handout/smf/
# http:#www.omega-art.com/midi/mfiles.html
# This exhausts theMeta event types in these documents.

Meta_Text            =    1
Meta_Copyright       =    2
Meta_SequenceName    =    3   # Or "track name"
Meta_InstrumentName  =    4
Meta_LyricText       =    5
Meta_MarkerText      =    6
Meta_CuePoint        =    7
Meta_UndefinedText1  = 0x08
Meta_UndefinedText2  = 0x09
Meta_UndefinedText3  = 0x0A # 10
Meta_UndefinedText4  = 0x0B # 11
Meta_UndefinedText5  = 0x0C # 12
Meta_UndefinedText6  = 0x0D # 13
Meta_UndefinedText7  = 0x0E # 14
Meta_UndefinedText8  = 0x0F  # 15

Meta_FirstText       = Meta_Text
Meta_LastText        = Meta_UndefinedText8

Meta_SequenceNumber  = 0x00
Meta_ChannelPrefix   = 0x20
Meta_PortPrefix      = 0x21
Meta_EndOfTrack      = 0x2F
Meta_TempoSetting    = 0x51
Meta_SMPTEOffset     = 0x54
Meta_TimeSignature   = 0x58
Meta_KeySignature    = 0x59
Meta_SequencerEvent  = 0x7F

# Returned by event.metaMessageType if self is not aMeta message.
Meta_None            = 0xFF

# prepared by Charles Gillingham cgillingham1@mac.com
