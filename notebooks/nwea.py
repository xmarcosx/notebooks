TEMPLATE = {
  "Maps": [
    {
      "Name": "NWEA-MAP_DataMap",
      "ResourcePath": "/ed-fi/studentAssessments",
      "ColumnHeaders": [
        "TermName",
        "StudentID",
        "SchoolName",
        "MeasurementScale",
        "Discipline",
        "GrowthMeasureYN",
        "NormsReferenceData",
        "WISelectedAYFall",
        "WISelectedAYWinter",
        "WISelectedAYSpring",
        "WIPreviousAYFall",
        "WIPreviousAYWinter",
        "WIPreviousAYSpring",
        "TestType",
        "TestName",
        "TestID",
        "TestStartDate",
        "TestDurationMinutes",
        "TestRITScore",
        "TestStandardError",
        "TestPercentile",
        "FallToFallProjectedGrowth",
        "FallToFallObservedGrowth",
        "FallToFallObservedGrowthSE",
        "FallToFallMetProjectedGrowth",
        "FallToFallConditionalGrowthIndex",
        "FallToFallConditionalGrowthPercentile",
        "FallToWinterProjectedGrowth",
        "FallToWinterObservedGrowth",
        "FallToWinterObservedGrowthSE",
        "FallToWinterMetProjectedGrowth",
        "FallToWinterConditionalGrowthIndex",
        "FallToWinterConditionalGrowthPercentile",
        "FallToSpringProjectedGrowth",
        "FallToSpringObservedGrowth",
        "FallToSpringObservedGrowthSE",
        "FallToSpringMetProjectedGrowth",
        "FallToSpringConditionalGrowthIndex",
        "FallToSpringConditionalGrowthPercentile",
        "WinterToWinterProjectedGrowth",
        "WinterToWinterObservedGrowth",
        "WinterToWinterObservedGrowthSE",
        "WinterToWinterMetProjectedGrowth",
        "WinterToWinterConditionalGrowthIndex",
        "WinterToWinterConditionalGrowthPercentile",
        "WinterToSpringProjectedGrowth",
        "WinterToSpringObservedGrowth",
        "WinterToSpringObservedGrowthSE",
        "WinterToSpringMetProjectedGrowth",
        "WinterToSpringConditionalGrowthIndex",
        "WinterToSpringConditionalGrowthPercentile",
        "SpringToSpringProjectedGrowth",
        "SpringToSpringObservedGrowth",
        "SpringToSpringObservedGrowthSE",
        "SpringToSpringMetProjectedGrowth",
        "SpringToSpringConditionalGrowthIndex",
        "SpringToSpringConditionalGrowthPercentile",
        "RITtoReadingScore",
        "RITtoReadingMin",
        "RITtoReadingMax",
        "Goal1Name",
        "Goal1RitScore",
        "Goal1StdErr",
        "Goal1Range",
        "Goal1Adjective",
        "Goal2Name",
        "Goal2RitScore",
        "Goal2StdErr",
        "Goal2Range",
        "Goal2Adjective",
        "Goal3Name",
        "Goal3RitScore",
        "Goal3StdErr",
        "Goal3Range",
        "Goal3Adjective",
        "Goal4Name",
        "Goal4RitScore",
        "Goal4StdErr",
        "Goal4Range",
        "Goal4Adjective",
        "Goal5Name",
        "Goal5RitScore",
        "Goal5StdErr",
        "Goal5Range",
        "Goal5Adjective",
        "Goal6Name",
        "Goal6RitScore",
        "Goal6StdErr",
        "Goal6Range",
        "Goal6Adjective",
        "Goal7Name",
        "Goal7RitScore",
        "Goal7StdErr",
        "Goal7Range",
        "Goal7Adjective",
        "Goal8Name",
        "Goal8RitScore",
        "Goal8StdErr",
        "Goal8Range",
        "Goal8Adjective",
        "TestStartTime",
        "PercentCorrect",
        "ProjectedProficiencyStudy1",
        "ProjectedProficiencyLevel1",
        "ProjectedProficiencyStudy2",
        "ProjectedProficiencyLevel2",
        "ProjectedProficiencyStudy3",
        "ProjectedProficiencyLevel3",
        "TypicalFallToFallGrowth",
        "TypicalFallToWinterGrowth",
        "TypicalFallToSpringGrowth",
        "TypicalWinterToWinterGrowth",
        "TypicalWinterToSpringGrowth",
        "TypicalSpringToSpringGrowth",
        "ProjectedProficiencyStudy4",
        "ProjectedProficiencyLevel4",
        "ProjectedProficiencyStudy5",
        "ProjectedProficiencyLevel5",
        "ProjectedProficiencyStudy6",
        "ProjectedProficiencyLevel6",
        "ProjectedProficiencyStudy7",
        "ProjectedProficiencyLevel7",
        "ProjectedProficiencyStudy8",
        "ProjectedProficiencyLevel8",
        "ProjectedProficiencyStudy9",
        "ProjectedProficiencyLevel9",
        "ProjectedProficiencyStudy10",
        "ProjectedProficiencyLevel10"
      ],
      "Map": {
        "studentAssessmentIdentifier": {
          "Column": "TestID"
        },
        "assessmentReference": {
          "assessmentIdentifier": "NWEA-MAP-V1",
          "namespace": "uri://www.nwea.org/map/Assessment"
        },
        "schoolYearTypeReference": {
          "schoolYear": {
            "Column": "TermName",
            "Lookup": "NWEA-MAP_SchoolYear"
          }
        },
        "studentReference": {
          "studentUniqueId": {
            "Column": "StudentID"
          }
        },
        "administrationDate": {
          "Column": "TestStartDate"
        },
        "performanceLevels": [
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Growth Measure YN",
            "performanceLevelDescriptor": {
              "Column": "GrowthMeasureYN",
              "Lookup": "NWEA-MAP_GrowthMeasure"
            },
            "performanceLevelMet": true
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Met Projected Growth",
            "performanceLevelDescriptor": {
              "Column": "FallToFallMetProjectedGrowth",
              "Lookup": "NWEA-MAP_MetProjectedGrowth"
            },
            "performanceLevelMet": true
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": {
              "Column": "FallToWinterMetProjectedGrowth",
              "Lookup": "NWEA-MAP_MetProjectedGrowth"
            },
            "performanceLevelMet": true
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": {
              "Column": "FallToSpringMetProjectedGrowth",
              "Lookup": "NWEA-MAP_MetProjectedGrowth"
            },
            "performanceLevelMet": true
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": {
              "Column": "WinterToWinterMetProjectedGrowth",
              "Lookup": "NWEA-MAP_MetProjectedGrowth"
            },
            "performanceLevelMet": true
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": {
              "Column": "WinterToSpringMetProjectedGrowth",
              "Lookup": "NWEA-MAP_MetProjectedGrowth"
            },
            "performanceLevelMet": true
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": {
              "Column": "SpringToSpringMetProjectedGrowth",
              "Lookup": "NWEA-MAP_MetProjectedGrowth"
            },
            "performanceLevelMet": true
          }
        ],
        "scoreResults": [
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Term Name",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "TermName"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Measurement Scale",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "MeasurementScale"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Test Name",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "TestName"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "TestRITScore"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "TestStandardError"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "TestPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToFallProjectedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToFallObservedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "FallToFallObservedGrowthSE"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "FallToFallConditionalGrowthIndex"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToFallConditionalGrowthPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToWinterProjectedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToWinterObservedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "FallToWinterObservedGrowthSE"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "FallToWinterConditionalGrowthIndex"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToWinterConditionalGrowthPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToSpringProjectedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToSpringObservedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "FallToSpringObservedGrowthSE"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "FallToSpringConditionalGrowthIndex"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "FallToSpringConditionalGrowthPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "WinterToWinterProjectedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "WinterToWinterObservedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "WinterToWinterObservedGrowthSE"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "WinterToWinterConditionalGrowthIndex"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "WinterToWinterConditionalGrowthPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "WinterToSpringProjectedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "WinterToSpringObservedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "WinterToSpringObservedGrowthSE"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "WinterToSpringConditionalGrowthIndex"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "WinterToSpringConditionalGrowthPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "SpringToSpringProjectedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "SpringToSpringObservedGrowth"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "SpringToSpringObservedGrowthSE"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
            "result": {
              "Column": "SpringToSpringConditionalGrowthIndex"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
            "result": {
              "Column": "SpringToSpringConditionalGrowthPercentile"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#RIT to Reading Score",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "RITtoReadingScore"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#RIT to Reading Min",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "RITtoReadingMin"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#RIT to Reading Max",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "RITtoReadingMax"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-1",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel1"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-2",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel2"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-3",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel3"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-4",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel4"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-5",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel5"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-6",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel6"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-7",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel7"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-8",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel8"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-9",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel9"
            }
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-10",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level",
            "result": {
              "Column": "ProjectedProficiencyLevel10"
            }
          }
        ],
        "studentObjectiveAssessments": [
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-1",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal1Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal1RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal1StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal1Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-2",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal2Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal2RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal2StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal2Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-3",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal3Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal3RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal3StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal3Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-4",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal4Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal4RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal4StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal4Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-5",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal5Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal5RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal5StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal5Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-6",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal6Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal6RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal6StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal6Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-7",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal7Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal7RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal7StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal7Range"
                }
              }
            ]
          },
          {
            "objectiveAssessmentReference": {
              "assessmentIdentifier": "NWEA-MAP-V1",
              "identificationCode": "NWEA-MAP-V1-GOAL-8",
              "namespace": "uri://www.nwea.org/map/Assessment"
            },
            "performanceLevels": [
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
                "performanceLevelDescriptor": {
                  "Column": "Goal8Adjective",
                  "Lookup": "NWEA-MAP_GoalAdjective"
                },
                "performanceLevelMet": true
              }
            ],
            "scoreResults": [
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer",
                "result": {
                  "Column": "Goal8RitScore"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal",
                "result": {
                  "Column": "Goal8StdErr"
                }
              },
              {
                "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
                "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range",
                "result": {
                  "Column": "Goal8Range"
                }
              }
            ]
          }
        ]
      }
    }
  ],
  "Bootstraps": [
    {
      "Name": "NWEA-MAP_ARMD",
      "ResourcePath": "/ed-fi/assessmentReportingMethodDescriptors",
      "Data": [
        {
          "codeValue": "Term Name",
          "description": "Term Name",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Term Name"
        },
        {
          "codeValue": "Measurement Scale",
          "description": "Specific RIT scale that applies  to the associated test.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Measurement Scale"
        },
        {
          "codeValue": "Growth Measure YN",
          "description": "When more than one result record exists for a given student and test, only one record counts for growth reporting, marked TRUE.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Growth Measure YN"
        },
        {
          "codeValue": "Test Name",
          "description": "Full name of the test.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Test Name"
        },
        {
          "codeValue": "Fall-To-Fall Projected Growth",
          "description": "Projected RIT growth from previous academic year fall term to the fall term chosen at export. Based on previous fall term RIT score and weeks of instruction.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Fall Projected Growth"
        },
        {
          "codeValue": "Fall-To-Fall Observed Growth",
          "description": "Actual growth from previous academic year fall term to the fall term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Fall Observed Growth"
        },
        {
          "codeValue": "Fall-To-Fall Observed Growth SE",
          "description": "Standard Error associated with calculation for FalltoFallObservedGrowth.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Fall Observed Growth SE"
        },
        {
          "codeValue": "Fall-To-Fall Met Projected Growth",
          "description": "Whether Projected Growth was met or not. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Fall Met Projected Growth"
        },
        {
          "codeValue": "Fall-To-Fall Conditional Growth Index",
          "description": "Calculation that enables you to compare student growth. Measures growth from the previous academic year fall term to the fall term chosen at export. It incorporates: -weeks of instruction before testing -how high students scored in the first term.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Fall Conditional Growth Index"
        },
        {
          "codeValue": "Fall-To-Fall Conditional Growth Percentile",
          "description": "Translates the Conditional Growth Index to national percentile rankings for growth. Measures growth from the previous academic year fall term to the fall term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Fall Conditional Growth Percentile"
        },
        {
          "codeValue": "Fall-To-Winter Projected Growth",
          "description": "Projected RIT growth from previous academic year fall term to the winter term chosen at export. Based on previous fall term RIT score and weeks of instruction.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Winter Projected Growth"
        },
        {
          "codeValue": "Fall-To-Winter Observed Growth",
          "description": "Actual growth from previous academic year fall term to the winter term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Winter Observed Growth"
        },
        {
          "codeValue": "Fall-To-Winter Observed Growth SE",
          "description": "Standard Error associated with calculation for FalltoWinterObservedGrowth.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Winter Observed Growth SE"
        },
        {
          "codeValue": "Fall-To-Winter Met Projected Growth",
          "description": "Whether Projected Growth was met or not. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Winter Met Projected Growth"
        },
        {
          "codeValue": "Fall-To-Winter Conditional Growth Index",
          "description": "Calculation that enables you to compare student growth. Measures growth from the previous academic year fall term to the winter term chosen at export. It incorporates: -weeks of instruction before testing -how high students scored in the first term.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Winter Conditional Growth Index"
        },
        {
          "codeValue": "Fall-To-Winter Conditional Growth Percentile",
          "description": "Translates the Conditional Growth Index to national percentile rankings for growth. Measures growth from the previous academic year fall term to the winter term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Winter Conditional Growth Percentile"
        },
        {
          "codeValue": "Fall-To-Spring Projected Growth",
          "description": "Projected RIT growth from previous academic year fall term to the spring term chosen at export.  Based on previous fall term RIT score and weeks of instruction.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Spring Projected Growth"
        },
        {
          "codeValue": "Fall-To-Spring Observed Growth",
          "description": "Actual growth from previous academic year fall term to the spring term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Spring Observed Growth"
        },
        {
          "codeValue": "Fall-To-Spring Observed Growth SE",
          "description": "Standard Error associated with calculation for FalltoSpringObservedGrowth.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Spring Observed Growth SE"
        },
        {
          "codeValue": "Fall-To-Spring Met Projected Growth",
          "description": "Whether Projected Growth was met or not. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Spring Met Projected Growth"
        },
        {
          "codeValue": "Fall-To-Spring Conditional Growth Index",
          "description": "Calculation that enables you to compare student growth. Measures growth from the previous academic year fall term to the spring term chosen at export. It incorporates: -weeks of instruction before testing -how high students scored in the first term.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Spring Conditional Growth Index"
        },
        {
          "codeValue": "Fall-To-Spring Conditional Growth Percentile",
          "description": "Translates the Conditional Growth Index to national percentile rankings for growth. Measures growth from the previous academic year fall term to the spring term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Fall-To-Spring Conditional Growth Percentile"
        },
        {
          "codeValue": "Winter-To-Winter Projected Growth",
          "description": "Projected RIT growth from previous academic year winter term to the winter term chosen at export.  Based on previous fall term RIT score and weeks of instruction.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Winter Projected Growth"
        },
        {
          "codeValue": "Winter-To-Winter Observed Growth",
          "description": "Actual growth from previous academic year winter term to the winter term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Winter Observed Growth"
        },
        {
          "codeValue": "Winter-To-Winter Observed Growth SE",
          "description": "Standard Error associated with calculation for FalltoSpringObservedGrowth.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Winter Observed Growth SE"
        },
        {
          "codeValue": "Winter-To-Winter Met Projected Growth",
          "description": "Whether Projected Growth was met or not. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Winter Met Projected Growth"
        },
        {
          "codeValue": "Winter-To-Winter Conditional Growth Index",
          "description": "Calculation that enables you to compare student growth. Measures growth from the previous academic year winter term to the winter term chosen at export. It incorporates: -weeks of instruction before testing -how high students scored in the first term.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Winter Conditional Growth Index"
        },
        {
          "codeValue": "Winter-To-Winter Conditional Growth Percentile",
          "description": "Translates the Conditional Growth Index to national percentile rankings for growth. Measures growth from the previous academic year winter term to the winter term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Winter Conditional Growth Percentile"
        },
        {
          "codeValue": "Winter-To-Spring Projected Growth",
          "description": "Projected RIT growth from previous academic year winter term to spring term chosen at export.  Based on previous fall term RIT score and weeks of instruction.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Spring Projected Growth"
        },
        {
          "codeValue": "Winter-To-Spring Observed Growth",
          "description": "Actual growth from previous academic year winter term to spring term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Spring Observed Growth"
        },
        {
          "codeValue": "Winter-To-Spring Observed Growth SE",
          "description": "Standard Error associated with calculation for FalltoSpringObservedGrowth.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Spring Observed Growth SE"
        },
        {
          "codeValue": "Winter-To-Spring Met Projected Growth",
          "description": "Whether Projected Growth was met or not. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Spring Met Projected Growth"
        },
        {
          "codeValue": "Winter-To-Spring Conditional Growth Index",
          "description": "Calculation that enables you to compare student growth. Measures growth from the previous academic year winter term to spring term chosen at export. It incorporates: -weeks of instruction before testing -how high students scored in the first term.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Spring Conditional Growth Index"
        },
        {
          "codeValue": "Winter-To-Spring Conditional Growth Percentile",
          "description": "Translates the Conditional Growth Index to national percentile rankings for growth. Measures growth from the previous academic year winter term to spring term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Winter-To-Spring Conditional Growth Percentile"
        },
        {
          "codeValue": "Spring-To-Spring Projected Growth",
          "description": "Projected RIT growth from previous academic year spring term to spring term chosen at export.  Based on previous fall term RIT score and weeks of instruction.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Spring-To-Spring Projected Growth"
        },
        {
          "codeValue": "Spring-To-Spring Observed Growth",
          "description": "Actual growth from previous academic year spring term to spring term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Spring-To-Spring Observed Growth"
        },
        {
          "codeValue": "Spring-To-Spring Observed Growth SE",
          "description": "Standard Error associated with calculation for FalltoSpringObservedGrowth.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Spring-To-Spring Observed Growth SE"
        },
        {
          "codeValue": "Spring-To-Spring Met Projected Growth",
          "description": "Whether Projected Growth was met or not. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Spring-To-Spring Met Projected Growth"
        },
        {
          "codeValue": "Spring-To-Spring Conditional Growth Index",
          "description": "Calculation that enables you to compare student growth. Measures growth from the previous academic year spring term to spring term chosen at export. It incorporates: -weeks of instruction before testing -how high students scored in the first term. ",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Spring-To-Spring Conditional Growth Index"
        },
        {
          "codeValue": "Spring-To-Spring Conditional Growth Percentile",
          "description": "Translates the Conditional Growth Index to national percentile rankings for growth. Measures growth from the previous academic year spring term to spring term chosen at export.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Spring-To-Spring Conditional Growth Percentile"
        },
        {
          "codeValue": "RIT to Reading Score",
          "description": "Score resulting from a correlation between NWEA’s RIT score and the Lexile®  scale (a measure defined by MetaMetrics®). Available only for Reading tests.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "RIT to Reading Score"
        },
        {
          "codeValue": "RIT to Reading Min",
          "description": "Lower end of the RIT to Reading Range.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "RIT to Reading Min"
        },
        {
          "codeValue": "RIT to Reading Max",
          "description": "Upper end of the RIT to Reading Range.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "RIT to Reading Max"
        },
        {
          "codeValue": "Goal Name",
          "description": "Name of goal for a section of the test.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Goal Name"
        },
        {
          "codeValue": "Goal Range",
          "description": "RIT range based on the standard error and RIT score.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Goal Range"
        },
        {
          "codeValue": "Goal Adjective",
          "description": "Goal adjective related to the goal score. This is defined using the goal score percentile as it relates to a norm set and its associative cut sheet.",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Goal Adjective"
        },
        {
          "codeValue": "Projected Proficiency Study-1",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-1"
        },
        {
          "codeValue": "Projected Proficiency Level-1",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-1"
        },
        {
          "codeValue": "Projected Proficiency Study-2",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-2"
        },
        {
          "codeValue": "Projected Proficiency Level-2",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-2"
        },
        {
          "codeValue": "Projected Proficiency Study-3",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-3"
        },
        {
          "codeValue": "Projected Proficiency Level-3",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-3"
        },
        {
          "codeValue": "Projected Proficiency Study-4",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-4"
        },
        {
          "codeValue": "Projected Proficiency Level-4",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-4"
        },
        {
          "codeValue": "Projected Proficiency Study-5",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-5"
        },
        {
          "codeValue": "Projected Proficiency Level-5",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-5"
        },
        {
          "codeValue": "Projected Proficiency Study-6",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-6"
        },
        {
          "codeValue": "Projected Proficiency Level-6",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-6"
        },
        {
          "codeValue": "Projected Proficiency Study-7",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-7"
        },
        {
          "codeValue": "Projected Proficiency Level-7",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-7"
        },
        {
          "codeValue": "Projected Proficiency Study-8",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-8"
        },
        {
          "codeValue": "Projected Proficiency Level-8",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-8"
        },
        {
          "codeValue": "Projected Proficiency Study-9",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-9"
        },
        {
          "codeValue": "Projected Proficiency Level-9",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-9"
        },
        {
          "codeValue": "Projected Proficiency Study-10",
          "description": "NWEA linking study associated with the MAP test taken",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Study-10"
        },
        {
          "codeValue": "Projected Proficiency Level-10",
          "description": "Projected proficiency level, or category, such as Unsatisfactory, Partially Proficient, and so on",
          "namespace": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor",
          "shortDescription": "Projected Proficiency Level-10"
        }
      ]
    },
    {
      "Name": "NWEA-MAP_PLD",
      "ResourcePath": "/ed-fi/performanceLevelDescriptors",
      "Data": [
        {
          "codeValue": "TRUE",
          "description": "TRUE",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "TRUE"
        },
        {
          "codeValue": "FALSE",
          "description": "FALSE",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "FALSE"
        },
        {
          "codeValue": "Yes",
          "description": "Student met growth projection.",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "Yes"
        },
        {
          "codeValue": "No",
          "description": "Growth projection not met. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "No"
        },
        {
          "codeValue": "Yes*",
          "description": "Student met growth projection.",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "Yes*"
        },
        {
          "codeValue": "No*",
          "description": "Growth projection not met. Asterisk means Observed Growth Standard Error (SE) could be large enough to put the outcome in question, so evaluate in combination with other points of data.",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "No*"
        },
        {
          "codeValue": "Low",
          "description": "Low (percentile <= 20)",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "Low"
        },
        {
          "codeValue": "LoAvg",
          "description": "LoAvg (percentile > 20 to <= 40)",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "LoAvg"
        },
        {
          "codeValue": "Avg",
          "description": "Avg (percentile > 40 to <= 60)",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "Avg"
        },
        {
          "codeValue": "HiAvg",
          "description": "HiAvg (percentile > 60 to <= 80)",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "HiAvg"
        },
        {
          "codeValue": "High",
          "description": "High (percentile > 80",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "High"
        },
        {
          "codeValue": "*",
          "description": "* goal adjective could not be computed)",
          "namespace": "uri://www.nwea.org/map/PerformanceLevelDescriptor",
          "shortDescription": "*"
        }
      ]
    },
    {
      "Name": "NWEA-MAP_Assessment",
      "ResourcePath": "/ed-fi/assessments",
      "Data": {
        "assessmentIdentifier": "NWEA-MAP-V1",
        "assessmentTitle": "NWEA-MAP-V1",
        "namespace": "uri://www.nwea.org/map/Assessment",
        "assessedGradeLevels": [
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Kindergarten"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#First grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Second grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Third grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Fourth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Fifth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Sixth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Seventh grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Eighth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Ninth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Tenth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Eleventh grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Twelfth grade"
          },
          {
            "gradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Ungraded"
          }
        ],
        "assessmentCategoryDescriptor": "uri://ed-fi.org/AssessmentCategoryDescriptor#Other",
        "academicSubjects": [
          {
            "academicSubjectDescriptor": "uri://ed-fi.org/AcademicSubjectDescriptor#Mathematics"
          },
          {
            "academicSubjectDescriptor": "uri://ed-fi.org/AcademicSubjectDescriptor#Reading"
          }
        ],
        "scores": [
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Term Name",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Measurement Scale",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Test Name",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Projected Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Observed Growth",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Observed Growth SE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Conditional Growth Index",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Conditional Growth Percentile",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#RIT to Reading Score",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#RIT to Reading Min",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#RIT to Reading Max",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-1",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-1",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-2",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-2",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-3",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-3",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-4",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-4",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-5",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-5",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-6",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-6",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-7",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-7",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-8",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-8",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-9",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-9",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Study-10",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Projected Proficiency Level-10",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          }
        ],
        "performanceLevels": [
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Growth Measure YN",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#TRUE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Growth Measure YN",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#FALSE",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Fall Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Fall-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Winter Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Winter-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          },
          {
            "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Spring-To-Spring Met Projected Growth",
            "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*",
            "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
          }
        ]
      }
    },
    {
      "Name": "NWEA-MAP_ObjectiveAssessments",
      "ResourcePath": "/ed-fi/objectiveAssessments",
      "Data": [
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-1",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-1",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-2",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-2",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-3",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-3",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-4",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-4",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-5",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-5",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-6",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-6",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-7",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-7",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        },
        {
          "identificationCode": "NWEA-MAP-V1-GOAL-8",
          "assessmentReference": {
            "assessmentIdentifier": "NWEA-MAP-V1",
            "namespace": "uri://www.nwea.org/map/Assessment"
          },
          "description": "Goal-8",
          "scores": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Name",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#RIT scale score",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Integer"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://ed-fi.org/AssessmentReportingMethodDescriptor#Standard error measurement",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Decimal"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Range",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Range"
            }
          ],
          "performanceLevels": [
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            },
            {
              "assessmentReportingMethodDescriptor": "uri://www.nwea.org/map/AssessmentReportingMethodDescriptor#Goal Adjective",
              "performanceLevelDescriptor": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*",
              "resultDatatypeTypeDescriptor": "uri://ed-fi.org/ResultDatatypeTypeDescriptor#Level"
            }
          ]
        }
      ]
    }
  ],
  "Lookups": [
    {
      "SourceTable": "NWEA-MAP_GoalAdjective",
      "Key": "*",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#*"
    },
    {
      "SourceTable": "NWEA-MAP_GoalAdjective",
      "Key": "Avg",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Avg"
    },
    {
      "SourceTable": "NWEA-MAP_GoalAdjective",
      "Key": "HiAvg",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#HiAvg"
    },
    {
      "SourceTable": "NWEA-MAP_GoalAdjective",
      "Key": "High",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#High"
    },
    {
      "SourceTable": "NWEA-MAP_GoalAdjective",
      "Key": "LoAvg",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#LoAvg"
    },
    {
      "SourceTable": "NWEA-MAP_GoalAdjective",
      "Key": "Low",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Low"
    },
    {
      "SourceTable": "NWEA-MAP_GrowthMeasure",
      "Key": "FALSE",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#FALSE"
    },
    {
      "SourceTable": "NWEA-MAP_GrowthMeasure",
      "Key": "TRUE",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#TRUE"
    },
    {
      "SourceTable": "NWEA-MAP_MetProjectedGrowth",
      "Key": "No",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No"
    },
    {
      "SourceTable": "NWEA-MAP_MetProjectedGrowth",
      "Key": "No*",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#No*"
    },
    {
      "SourceTable": "NWEA-MAP_MetProjectedGrowth",
      "Key": "Yes",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes"
    },
    {
      "SourceTable": "NWEA-MAP_MetProjectedGrowth",
      "Key": "Yes*",
      "Value": "uri://www.nwea.org/map/PerformanceLevelDescriptor#Yes*"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2015-2016",
      "Value": "2016"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2016-2017",
      "Value": "2017"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2017-2018",
      "Value": "2018"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2018-2019",
      "Value": "2019"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2019-2020",
      "Value": "2020"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2020-2021",
      "Value": "2021"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2021-2022",
      "Value": "2022"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2022-2023",
      "Value": "2023"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2023-2024",
      "Value": "2024"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2024-2025",
      "Value": "2025"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2025-2026",
      "Value": "2026"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2026-2027",
      "Value": "2027"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2027-2028",
      "Value": "2028"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2028-2029",
      "Value": "2029"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Fall 2029-2030",
      "Value": "2030"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2015-2016",
      "Value": "2016"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2016-2017",
      "Value": "2017"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2017-2018",
      "Value": "2018"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2018-2019",
      "Value": "2019"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2019-2020",
      "Value": "2020"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2020-2021",
      "Value": "2021"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2021-2022",
      "Value": "2022"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2022-2023",
      "Value": "2023"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2023-2024",
      "Value": "2024"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2024-2025",
      "Value": "2025"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2025-2026",
      "Value": "2026"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2026-2027",
      "Value": "2027"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2027-2028",
      "Value": "2028"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2028-2029",
      "Value": "2029"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Spring 2029-2030",
      "Value": "2030"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2015-2016",
      "Value": "2016"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2016-2017",
      "Value": "2017"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2017-2018",
      "Value": "2018"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2018-2019",
      "Value": "2019"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2019-2020",
      "Value": "2020"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2020-2021",
      "Value": "2021"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2021-2022",
      "Value": "2022"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2022-2023",
      "Value": "2023"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2023-2024",
      "Value": "2024"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2024-2025",
      "Value": "2025"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2025-2026",
      "Value": "2026"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2026-2027",
      "Value": "2027"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2027-2028",
      "Value": "2028"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2028-2029",
      "Value": "2029"
    },
    {
      "SourceTable": "NWEA-MAP_SchoolYear",
      "Key": "Winter 2029-2030",
      "Value": "2030"
    }
  ]
}