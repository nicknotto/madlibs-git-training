#!/usr/bin/python3
import json
__doc__ = """
Provides the MadLib object, a template for creating madlibs; see
the documentation of MadLib for instructions on how to properly subclass it for
creating new madlib generators.
 
An example madlib generator object, called TechnologyAdoptionLifecycle, is provided.
"""
 
__author__ = "Curtis Miller and Nick Notto"
__copyright__ = "Copyright (c) 2017, Curtis Grant Miller, and 2020, Nick Notto"
__credits__ = ["Nick Notto, based on https://ntguardian.wordpress.com/2017/10/06/mad-libs-and-python/ by Curtis Miller"]
__license__ = "All self._text is based on wikipedia using Creative Commons Attribution-ShareAlike 3.0 Unported License.  All else GPL."
__version__ = "0.1.0"
__maintainer__ = "Nick Notto"
__email__ = "n/a"
__status__ = "Experimental"
 
class MadLib(object):
    """An object for managing madlibs.
 
    A new madlib subclassed from this object should change only the __init__()
    method, and assign a new _text (string for formatting) & _descriptors (dict)
    _inputs should always be an empty dict (it's okay if
    it's not, but its contents will be reset by get_inputs(), so any content
    put there will do nothing). _text should be a string that the format()
    method can work with, being passed keys of a dict; an example of a valid
    _text is "One day, a {occupation1} {verb1} to a {place1} to buy {object1}s."
    _descriptors has keys corresponding to EVERY field in _text (errors will be
    thrown if this is not the case) and values that instruct users, in the
    prompt, what is desired. (So, for example, a key/value pair would be:
 
    "occupation1": "an occupation for a person (e.g. firefighter)"
 
    and so on.)
    """
    def __init__(self):
        """Initialization; get initial objects
 
        This is the only method changed when creating new madlibs. Declares
        _text and _descriptors
        """
 
        self._text = ""
        # self._descriptors = dict()
 
    def get_inputs(self,num):
        file_input = open('../input.json')
        json_objs = json.load(file_input)
        self._inputs = json_objs[num]
        file_input.close()

 
    def print_result(self):
        """Print the resulting mad-lib"""
        try:
            print(self._text.format(**self._inputs))
        except Exception as e:
            raise AssertionError("You should run get_inputs() first!")
 
class TechnologyAdoptionLifecycle(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Technology adoption life cycle",
                               "\n\nThe technology adoption lifecycle is a {adj1} model that describes the adoption or",
                               "acceptance of a new product or innovation. The process of adoption over time is",
                               "typically illustrated as a \"{musical_instrument} curve\". The model indicates that",
                               "the first group of people to use a new product is called \"innovators\", followed",
                               "by \"{adj2} adopters\". next come the {adj3} majority and {adj4} majority, and the last",
                               "group to eventually adopt a product are called \"{plural_noun}\" or \"phobics.\" For",
                               "example, a phobic may only use a cloud {noun} when it is the only remaining method",
                               "of performing a required task, but the phobic may not have an in-depth technical",
                               "knowledge of how to use the service.\n\n\n"])


class TechnologyEvangelist(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Technology Evangelist",
                               "\n\nA technology evangelist is a person who builds a critical mass of {noun1}",
                               "for a given technology, and then establishes it as a {adj1} standard in a market",
                               "that is subject to network effects. The word evangelism is borrowed from the context",
                               "of religious evangelism due to the similarity of sharing {noun2} about a particular",
                               "concept with the intention of having others {verb} that concept. This is typically",
                               "accomplished by showcasing the {adj2} uses and benefits of a technology to help",
                               "others understand how they can use it for themselves.\n\n\n"])

class TechnologyEvangelist2(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Technology Evangelist",
                               "\n\nProfessional technology evangelists are often employed by {plural_noun1} seeking to",
                               "establish their technologies as de facto standards. Their work could also entail the",
                               "{verb_ending_in_ing1} of personnel, including top managers so that they acquire",
                               "{plural_noun2} and competencies necessary to adopt new technology or new technological",
                               "initiative. There are even instances when technology evangelism becomes an aspect of",
                               "a {adj} position. \n\nOpen-source evangelists, on the other hand, operate {adverb}.",
                               "Evangelists also participate in {verb_ending_in_ing} open standards. Non-professional",
                               "technology evangelists may {verb} out of altruism or self-interest (e.g., to gain the",
                               "benefits of early adoption or network effect).\n\n\n"])

class TheInternet(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["The Internet",
                               "\n\nThe Internet (portmanteau of interconnected network) is the global system of",
                               "interconnected computer networks that uses the Internet protocol {noun1} (TCP/IP)",
                               "to {noun2} devices worldwide. It is a network of {plural_noun1} that consists of",
                               "private, public, academic, business, and government networks of local to global",
                               "scope, linked by a broad array of electronic, wireless, and optical networking",
                               "{plural_noun2}. The Internet carries a {adj} range of information {plural_noun3}",
                               "and services, such as the inter-linked hypertext documents and applications of the",
                               "World Wide Web (WWW), electronic mail, telephony, and file {verb_ending_in_ing}.\n\n\n"])

class TheInternet2(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["The Internet",
                               "\n\nThe origins of the Internet date back to the development of {noun1} switching",
                               "and {noun2} commissioned by the United States Department of {noun3} in the 1960s to",
                               "enable time-sharing of mainframe {plural_noun1}. The primary precursor network, the",
                               "ARPANET, initially served as a backbone for interconnection of regional academic and",
                               "military {plural_noun2} in the 1970s. The funding of the National {noun3} Foundation",
                               "Network as a new backbone in the 1980s, as well as private funding for other commercial",
                               "extensions, led to worldwide participation in the development of new networking",
                               "technologies, and the merger of many networks. The linking of commercial networks and",
                               "enterprises by the early 1990s marked the beginning of the transition to the modern",
                               "Internet, and generated a sustained exponential growth as generations of institutional,",
                               "personal, and {adj} computers were connected to the network. Although the Internet was",
                               "widely used by academia in the 1980s, commercialization incorporated its services and",
                               "{plural_noun3} into virtually every aspect of modern life.\n\n\n"])

class AI(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["AI",
                               "\n\nIn computer science, artificial intelligence (AI), sometimes called machine",
                               "intelligence, is intelligence demonstrated by {plural_noun1}, in contrast to the natural",
                               "intelligence displayed by humans and {plural_noun2}. {verb_ending_in_ing1}AI",
                               "{plural_noun3} define the field as the study of \"intelligent agents\": any device that",
                               "perceives its {noun} and takes actions that maximize its chance of successfully achieving",
                               "its goals. Colloquially, the term \"artificial intelligence\" is often used to describe",
                               "machines (or computers) that {verb} \"cognitive\" functions that humans associate with the",
                               "human mind, such as \"{verb_ending_in_ing2}\" and \"problem solving\".\n\n\n"])

class ReverseEngineeringOfSoftware(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Reverse Engineering of Software",
                               "\n\nIn 1990, the Institute of Electrical and Electronics Engineers (IEEE) defined reverse",
                               "engineering as \"the process of analyzing a subject system to {verb1} the system's components",
                               "and their interrelationships and to create representations of the system in another form or",
                               "at a {adj1} level of abstraction\", where the \"subject system\" is the end product of",
                               "software development. Reverse engineering is a process of examination only: the software",
                               "system under consideration is not modified (which would make it re-engineering or",
                               "{noun_ending_in_ing}). Reverse engineering can be performed from any stage of the {noun1}",
                               "cycle, not necessarily from the {adj2} end product. \n\nOn a related note, black {noun2}",
                               "testing in software engineering has a lot in common with reverse engineering. The tester",
                               "usually has the API, but their goals are to {verb2} bugs and undocumented features by bashing",
                               "the {noun3} from outside.\n\n\n"])

class Patch(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Patch",
                               "\n\nA patch is a set of changes to a computer program or its supporting data designed to update,",
                               "{verb}, or improve it. This includes fixing {noun1} vulnerabilities and other bugs, with such",
                               "patches usually being called {noun2} fixes, and improving the functionality, {noun3} or",
                               "performance.\n\nPatching makes possible the modification of compiled and machine language object",
                               "programs when the source code is {adj1}. This demands a thorough understanding of the inner",
                               "workings of the object code by the person creating the patch, which is difficult without close",
                               "study of the source code. For minor changes to software, it is often easier and more economical",
                               "to distribute patches to users rather than redistributing a newly recompiled or reassembled",
                               "program.\n\nAlthough meant to fix problems, poorly designed patches can sometimes introduce",
                               "{adj2} problems (see software regressions). In some special cases updates may knowingly break",
                               "the {noun4} or disable a device, for instance, by removing components for which the update",
                               "provider is no longer licensed.\n\n\n"])

class BillGates(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Bill Gates",
                               "\n\nWilliam Henry Gates III (born October 28, 1955) is an American business {noun1}, software",
                               "developer, investor, and philanthropist. He is best known as the co-founder of Microsoft",
                               "Corporation. During his career at Microsoft, Gates held the positions of chairman, chief",
                               "executive (noun2), president and chief software {noun3}, while also being the largest",
                               "individual {noun4} until May 2014. He is one of the best-known entrepreneurs and pioneers of",
                               "the microcomputer revolution of the 1970s and 1980s.\n\nBorn and raised in Seattle, Washington,",
                               "Gates co-founded Microsoft with childhood friend {celebrity} in 1975 in Albuquerque, New Mexico;",
                               "it went on to become the world's {adj} personal computer software company.\n\n\n"])

class InternetTroll(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Internet Troll",
                               "\n\nIn Internet slang, a troll is a {noun1} who starts quarrels or {verb1} people on the",
                               "Internet to {verb2} and sow discord by posting inflammatory and digressive, extraneous, or",
                               "off-topic messages in an online community (such as a newsgroup, forum, chat room, or blog)",
                               "with the intent of provoking {noun2} into displaying emotional responses and normalizing",
                               "tangential discussion, whether for the troll's amusement or a specific gain.\n\nBoth the noun",
                               "and the verb forms of \"troll\" are associated with Internet discourse. However, the word",
                               "has also been used more widely. Media attention in recent years has equated trolling with",
                               "{noun3} harassment. For example, the mass media have used \"troll\" to mean \"a person who",
                               "defaces Internet tribute sites with the aim of causing grief to {noun4}\".\n\n\n"])

class Bitcoin(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Bitcoin",
                               "\n\nBitcoin (₿) is a cryptocurrency. It is a decentralized digital {noun1} without a central",
                               "bank or single {noun2} that can be sent from user to user on the peer-to-peer bitcoin network",
                               "without the need for intermediaries.\n\nTransactions are verified by network {plural_noun1}",
                               "through cryptography and recorded in a public {verb1} ledger called a blockchain. Bitcoin was",
                               "invented in 2008 by an unknown person or group of people using the name Satoshi Nakamoto and",
                               "started in 2009 when its source code was {verb2} as open-source software. Bitcoins are {verb3}",
                               "as a reward for a process known as {verb_ending_in_ing}. They can be exchanged for other",
                               "currencies, {plural_noun2}, and services.\n\n\n"])

class DataBreach(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Data Breach",
                               "\n\nA data breach is the intentional or unintentional release of secure or private/confidential",
                               "{noun1} to an untrusted {noun2}. Other terms for this phenomenon include {adj1} {noun3}",
                               "disclosure, data leak, information leakage and also {noun4} spill. Incidents range from",
                               "concerted attacks by black hats, or individuals who hack for some kind of {adj2} gain,",
                               "associated with organized crime, political activists or {adj3} governments to careless disposal",
                               "of used computer equipment or data storage media and unhackable source.\n\nData breaches may",
                               "involve financial information such as credit card or bank details, personal health information",
                               "(PHI), Personally identifiable information (PII), {adj4} secrets of corporations or {adj5}",
                               "property. Most data breaches involve overexposed and vulnerable unstructured data – files,",
                               "documents, and sensitive information.\n\n\n"])

class AntiPattern(MadLib):
    def __init__(self):
        """initialization;"""
        # Original source:
        # wikipedia
        self._text = " ".join(["Anti-pattern",
                               "\n\nAn anti-pattern is a common response to a {adj1} problem that is usually ineffective and",
                               "risks being highly counterproductive. The term, coined in {year} by {person}, was inspired by",
                               "a book, {noun1} Patterns, which highlights a number of design patterns in software development",
                               "that its authors considered to be highly reliable and effective.\n\nThe term was popularized",
                               "{number} years later by the book AntiPatterns, which extended its use beyond the field of",
                               "software design to refer informally to any commonly reinvented but {adj2} solution to a problem.",
                               "Examples include analysis paralysis, cargo cult {noun2}, death march, groupthink and vendor",
                               "lock-in.\n\n\n"])

if __name__ == '__main__':
    num = 0
    madlibs = [TechnologyAdoptionLifecycle(),TechnologyEvangelist(),TechnologyEvangelist2(),TheInternet(),TheInternet2(),
                AI(),ReverseEngineeringOfSoftware(),Patch(),BillGates(),InternetTroll(),Bitcoin(),DataBreach(),AntiPattern()]
    for madlib in madlibs:
        madlib.get_inputs(num)
        madlib.print_result()
        num += 1
