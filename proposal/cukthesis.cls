%This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
%%%
% LaTeX class for documents submitted to AG-Bloemer
% This is just a guideline - modify as you like :)
% Last Update: 13-01-2017
% In case of questions/problems/proposals you can write, call or visit me
% http://cs.uni-paderborn.de/cuk/personal/sascha-brauer/
%%%
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cukthesis}[2017/01/13 RC1 A document class for documents submitted to AG-Bloemer]

\newif\ifgerman\germanfalse

\DeclareOption{german}{\germantrue}

\newif\ifproposal\proposalfalse

\DeclareOption{proposal}{\proposaltrue}
\DeclareOption{seminar}{\proposaltrue}

\ProcessOptions
\ifproposal
	\LoadClass[a4paper, 12pt, oneside, numbers=noenddot, bibliography=totoc]{scrartcl}
\else
	\LoadClass[a4paper, 12pt, twoside, openright, BCOR1.5cm, appendixprefix, cleardoublepage=empty, numbers=noenddot, bibliography=totoc]{scrbook}
\fi

\ifgerman
	\RequirePackage[ngerman]{babel}
\else
	\RequirePackage[english]{babel}
\fi
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}

% Some older versions of MiKTeX are still missing the scrlayer-scrpage package ... -.-'
\IfFileExists{scrlayer-scrpage.sty}
{
	\RequirePackage[automark,headsepline]{scrlayer-scrpage}
}{
	\RequirePackage{fancyhdr}
}

% Header and footer Layout depending on the loaded package
\ifproposal
	\IfFileExists{scrlayer-scrpage.sty}
	{
		\pagestyle{scrheadings}

		\clearpairofpagestyles
		\cfoot[\pagemark]{\pagemark}
		\chead{\headmark}
	}{
		\pagestyle{fancy}

		\lhead[]{}
		\rhead[]{}
		\chead[]{\rightmark}
		\cfoot{\thepage}

		\fancypagestyle{plain}{
		\fancyhf{}
		\cfoot{\thepage}
		\renewcommand{\headrulewidth}{0pt}
		\renewcommand{\footrulewidth}{0pt}
		}
	}

	\renewcommand{\sectionmark}[1]{\markright{\textsc{#1}}}
	\renewcommand{\subsectionmark}[1]{\markright{\textsl{\thesubsection~#1}}}
\else
	\IfFileExists{scrlayer-scrpage.sty}
	{
		\pagestyle{scrheadings}

		\clearpairofpagestyles
		\lefoot[\pagemark]{\pagemark}
		\rofoot[\pagemark]{\pagemark}
		\lehead{\headmark}
		\rohead{\headmark}
	}{
		\pagestyle{fancy}

		\lhead[\fancyplain{}{\leftmark}]{}
		\rhead[]{\fancyplain{}{\rightmark}}
		\lfoot[\fancyplain{\thepage}{\thepage}]{}
		\rfoot[]{\fancyplain{\thepage}{\thepage}}
		\cfoot[]{}

		\fancypagestyle{plain}{
		\fancyhf{}
		\fancyfoot[LE,RO]{\thepage}
		\renewcommand{\headrulewidth}{0pt}
		\renewcommand{\footrulewidth}{0pt}
		}
	}

	\renewcommand{\chaptermark}[1]{\markboth{\textsc{\thechapter~#1}}{}}
	\renewcommand{\sectionmark}[1]{\markright{\textsl{\thesection~#1}}}
\fi

% Essential math packages
\RequirePackage{amsmath,amsfonts,amssymb,amsthm,mathtools}

% Theorem style
\newtheoremstyle{thmstyle}
  {3pt}{3pt}{\itshape}{}{\bfseries}{}{.5em}
  {\thmname{#1}\thmnumber{ #2}\thmnote{ \textmd{(#3)}}}
\theoremstyle{thmstyle}

% Theorem environments
\ifproposal
	\newtheorem{definition}{Definition}[section]
\else
	\newtheorem{definition}{Definition}[chapter]
\fi
\newtheorem{lemma}[definition]{Lemma}
\newtheorem{problem}[definition]{Problem}

\ifgerman
	\newtheorem{proposition}[definition]{Satz}
	\newtheorem{theorem}[definition]{Satz}
	\newtheorem{corollary}[definition]{Korollar}
	\newtheorem{example}[definition]{Beispiel}
	\newtheorem{claim}[definition]{Behauptung}
	\newtheorem{remark}[definition]{Bemerkung}
	\newtheorem{observation}[definition]{Beobachtung}
\else
	\newtheorem{proposition}[definition]{Proposition}
	\newtheorem{theorem}[definition]{Theorem}
	\newtheorem{corollary}[definition]{Corollary}
	\newtheorem{example}[definition]{Example}
	\newtheorem{claim}[definition]{Claim}
	\newtheorem{remark}[definition]{Remark}
	\newtheorem{observation}[definition]{Observation}
\fi
