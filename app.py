import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
import yaml
import json

class PromptGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Prompt Generator")
        self.setGeometry(100, 100, 800, 600)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Form layout
        form_layout = QVBoxLayout()

        # Version and Timestamp
        form_layout.addWidget(QLabel("Version:"))
        self.version_input = QLineEdit("3.1")
        form_layout.addWidget(self.version_input)

        form_layout.addWidget(QLabel("Timestamp (YYYY-MM-DDTHH:MM:SS-03:00):"))
        self.timestamp_input = QLineEdit("2025-08-31T20:13:00-03:00")
        form_layout.addWidget(self.timestamp_input)

        # Language
        form_layout.addWidget(QLabel("Language:"))
        self.language_combo = QComboBox()
        self.language_combo.addItems(["pt-BR", "en-US", "es-ES"])
        form_layout.addWidget(self.language_combo)

        # Language Strictness
        form_layout.addWidget(QLabel("Language Strictness:"))
        self.language_strictness_combo = QComboBox()
        self.language_strictness_combo.addItems(["strict_no_mixing", "flexible"])
        form_layout.addWidget(self.language_strictness_combo)

        # Protocol Strictness
        form_layout.addWidget(QLabel("Protocol Strictness:"))
        self.protocol_strictness_combo = QComboBox()
        self.protocol_strictness_combo.addItems(["high", "medium", "low"])
        form_layout.addWidget(self.protocol_strictness_combo)

        # Context
        context_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Context"))
        self.domain_input = QLineEdit()
        context_layout.addWidget(QLabel("Domain:"))
        context_layout.addWidget(self.domain_input)
        self.subdomain_input = QLineEdit()
        context_layout.addWidget(QLabel("Subdomain:"))
        context_layout.addWidget(self.subdomain_input)
        self.specific_topic_input = QLineEdit()
        context_layout.addWidget(QLabel("Specific Topic:"))
        context_layout.addWidget(self.specific_topic_input)
        self.geographical_scope_input = QLineEdit()
        context_layout.addWidget(QLabel("Geographical Scope:"))
        context_layout.addWidget(self.geographical_scope_input)
        self.historical_period_input = QLineEdit()
        context_layout.addWidget(QLabel("Historical Period:"))
        context_layout.addWidget(self.historical_period_input)
        form_layout.addLayout(context_layout)

        # Task
        task_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Task"))
        self.task_type_combo = QComboBox()
        self.task_type_combo.addItems(["comprehensive_guide_generation", "analysis", "synthesis", "tutorial"])
        task_layout.addWidget(QLabel("Task Type:"))
        task_layout.addWidget(self.task_type_combo)
        self.task_goal_input = QLineEdit()
        task_layout.addWidget(QLabel("Task Goal:"))
        task_layout.addWidget(self.task_goal_input)
        form_layout.addLayout(task_layout)

        # Constraints
        constraints_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Constraints"))
        self.word_limit_input = QLineEdit("null")
        constraints_layout.addWidget(QLabel("Word Limit:"))
        constraints_layout.addWidget(self.word_limit_input)
        self.tone_combo = QComboBox()
        self.tone_combo.addItems(["educational", "formal", "informal", "technical"])
        constraints_layout.addWidget(QLabel("Tone:"))
        constraints_layout.addWidget(self.tone_combo)
        self.audience_combo = QComboBox()
        self.audience_combo.addItems(["beginners_to_experts", "beginners", "intermediate", "experts"])
        constraints_layout.addWidget(QLabel("Audience:"))
        constraints_layout.addWidget(self.audience_combo)
        self.language_adherence_input = QLineEdit("exclusively_portuguese")
        constraints_layout.addWidget(QLabel("Language Adherence:"))
        constraints_layout.addWidget(self.language_adherence_input)
        self.technical_accuracy_input = QLineEdit("peer_review_level")
        constraints_layout.addWidget(QLabel("Technical Accuracy:"))
        constraints_layout.addWidget(self.technical_accuracy_input)
        self.citation_requirement_input = QLineEdit("mandatory")
        constraints_layout.addWidget(QLabel("Citation Requirement:"))
        constraints_layout.addWidget(self.citation_requirement_input)
        form_layout.addLayout(constraints_layout)

        # Content
        content_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Content"))
        self.main_question_input = QTextEdit()
        content_layout.addWidget(QLabel("Main Question:"))
        content_layout.addWidget(self.main_question_input)
        self.subquestions_input = QTextEdit()
        content_layout.addWidget(QLabel("Subquestions (one per line):"))
        content_layout.addWidget(self.subquestions_input)
        self.examples_input = QTextEdit()
        content_layout.addWidget(QLabel("Examples (JSON format, one per line):"))
        content_layout.addWidget(self.examples_input)
        self.additional_resources_input = QTextEdit()
        content_layout.addWidget(QLabel("Additional Resources (one per line):"))
        content_layout.addWidget(self.additional_resources_input)
        form_layout.addLayout(content_layout)

        # Response Format
        response_format_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Response Format"))
        self.structure_type_combo = QComboBox()
        self.structure_type_combo.addItems(["progressive_levels", "linear", "hierarchical"])
        response_format_layout.addWidget(QLabel("Structure Type:"))
        response_format_layout.addWidget(self.structure_type_combo)
        self.sections_input = QTextEdit()
        response_format_layout.addWidget(QLabel("Sections (one per line):"))
        response_format_layout.addWidget(self.sections_input)
        self.output_type_combo = QComboBox()
        self.output_type_combo.addItems(["detailed_text_with_tables_and_diagrams_descriptions", "text_only", "code_only", "multimedia"])
        response_format_layout.addWidget(QLabel("Output Type:"))
        response_format_layout.addWidget(self.output_type_combo)
        self.format_consistency_input = QLineEdit("strict_apa")
        response_format_layout.addWidget(QLabel("Format Consistency:"))
        response_format_layout.addWidget(self.format_consistency_input)
        self.section_length_input = QLineEdit("balanced")
        response_format_layout.addWidget(QLabel("Section Length:"))
        response_format_layout.addWidget(self.section_length_input)
        self.cross_referencing_input = QLineEdit("mandatory")
        response_format_layout.addWidget(QLabel("Cross Referencing:"))
        response_format_layout.addWidget(self.cross_referencing_input)
        form_layout.addLayout(response_format_layout)

        # Feedback Mechanism
        feedback_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Feedback Mechanism"))
        self.feedback_expected_combo = QComboBox()
        self.feedback_expected_combo.addItems(["true", "false"])
        feedback_layout.addWidget(QLabel("Feedback Expected:"))
        feedback_layout.addWidget(self.feedback_expected_combo)
        self.feedback_format_combo = QComboBox()
        self.feedback_format_combo.addItems(["json", "text"])
        feedback_layout.addWidget(QLabel("Feedback Format:"))
        feedback_layout.addWidget(self.feedback_format_combo)
        self.feedback_fields_input = QTextEdit()
        feedback_layout.addWidget(QLabel("Feedback Fields (one per line):"))
        feedback_layout.addWidget(self.feedback_fields_input)
        self.feedback_frequency_input = QLineEdit("per_section")
        feedback_layout.addWidget(QLabel("Feedback Frequency:"))
        feedback_layout.addWidget(self.feedback_frequency_input)
        form_layout.addLayout(feedback_layout)

        # Additional Parameters
        additional_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Additional Parameters"))
        self.depth_level_combo = QComboBox()
        self.depth_level_combo.addItems(["from_basic_to_advanced", "basic_only", "advanced_only"])
        additional_layout.addWidget(QLabel("Depth Level:"))
        additional_layout.addWidget(self.depth_level_combo)
        self.max_tokens_usage_combo = QComboBox()
        self.max_tokens_usage_combo.addItems(["maximum_possible", "limited_to_1000", "custom_limit"])
        additional_layout.addWidget(QLabel("Max Tokens Usage:"))
        additional_layout.addWidget(self.max_tokens_usage_combo)
        self.include_diagrams_combo = QComboBox()
        self.include_diagrams_combo.addItems(["true", "false"])
        additional_layout.addWidget(QLabel("Include Diagrams:"))
        additional_layout.addWidget(self.include_diagrams_combo)
        self.historical_context_combo = QComboBox()
        self.historical_context_combo.addItems(["detailed_timeline", "brief_overview"])
        additional_layout.addWidget(QLabel("Historical Context:"))
        additional_layout.addWidget(self.historical_context_combo)
        self.future_trends_combo = QComboBox()
        self.future_trends_combo.addItems(["speculative_insights", "current_trends_only"])
        additional_layout.addWidget(QLabel("Future Trends:"))
        additional_layout.addWidget(self.future_trends_combo)
        self.case_studies_combo = QComboBox()
        self.case_studies_combo.addItems(["real_world_examples", "hypothetical_scenarios"])
        additional_layout.addWidget(QLabel("Case Studies:"))
        additional_layout.addWidget(self.case_studies_combo)
        self.comparisons_combo = QComboBox()
        self.comparisons_combo.addItems(["tabular_formats", "narrative_comparisons"])
        additional_layout.addWidget(QLabel("Comparisons:"))
        additional_layout.addWidget(self.comparisons_combo)
        self.glossary_combo = QComboBox()
        self.glossary_combo.addItems(["key_terms_definitions", "none"])
        additional_layout.addWidget(QLabel("Glossary:"))
        additional_layout.addWidget(self.glossary_combo)
        self.quizzes_combo = QComboBox()
        self.quizzes_combo.addItems(["self_assessment_questions", "none"])
        additional_layout.addWidget(QLabel("Quizzes:"))
        additional_layout.addWidget(self.quizzes_combo)
        self.references_combo = QComboBox()
        self.references_combo.addItems(["expanded_bibliography", "minimal_references"])
        additional_layout.addWidget(QLabel("References:"))
        additional_layout.addWidget(self.references_combo)
        self.prerequisites_combo = QComboBox()
        self.prerequisites_combo.addItems(["none_assumed", "basic_knowledge_required"])
        additional_layout.addWidget(QLabel("Prerequisites:"))
        additional_layout.addWidget(self.prerequisites_combo)
        self.interactivity_suggestions_combo = QComboBox()
        self.interactivity_suggestions_combo.addItems(["links_to_simulations", "none"])
        additional_layout.addWidget(QLabel("Interactivity Suggestions:"))
        additional_layout.addWidget(self.interactivity_suggestions_combo)
        self.visual_aids_combo = QComboBox()
        self.visual_aids_combo.addItems(["ascii_art_diagrams", "none"])
        additional_layout.addWidget(QLabel("Visual Aids:"))
        additional_layout.addWidget(self.visual_aids_combo)
        self.error_handling_combo = QComboBox()
        self.error_handling_combo.addItems(["common_pitfalls_section", "none"])
        additional_layout.addWidget(QLabel("Error Handling:"))
        additional_layout.addWidget(self.error_handling_combo)
        self.performance_metrics_combo = QComboBox()
        self.performance_metrics_combo.addItems(["speed_latency_comparisons", "none"])
        additional_layout.addWidget(QLabel("Performance Metrics:"))
        additional_layout.addWidget(self.performance_metrics_combo)
        self.ensure_no_english_combo = QComboBox()
        self.ensure_no_english_combo.addItems(["true", "false"])
        additional_layout.addWidget(QLabel("Ensure No English:"))
        additional_layout.addWidget(self.ensure_no_english_combo)
        self.translation_check_combo = QComboBox()
        self.translation_check_combo.addItems(["self_validate", "none"])
        additional_layout.addWidget(QLabel("Translation Check:"))
        additional_layout.addWidget(self.translation_check_combo)
        self.term_consistency_combo = QComboBox()
        self.term_consistency_combo.addItems(["uniform_portuguese_terms", "flexible"])
        additional_layout.addWidget(QLabel("Term Consistency:"))
        additional_layout.addWidget(self.term_consistency_combo)
        self.audience_adaptation_combo = QComboBox()
        self.audience_adaptation_combo.addItems(["layered_explanations", "uniform_explanation"])
        additional_layout.addWidget(QLabel("Audience Adaptation:"))
        additional_layout.addWidget(self.audience_adaptation_combo)
        self.section_transitions_combo = QComboBox()
        self.section_transitions_combo.addItems(["smooth_progression", "abrupt_transitions"])
        additional_layout.addWidget(QLabel("Section Transitions:"))
        additional_layout.addWidget(self.section_transitions_combo)
        self.citation_style_combo = QComboBox()
        self.citation_style_combo.addItems(["apa_in_text", "mla", "chicago", "none"])
        additional_layout.addWidget(QLabel("Citation Style:"))
        additional_layout.addWidget(self.citation_style_combo)
        self.index_creation_combo = QComboBox()
        self.index_creation_combo.addItems(["true", "false"])
        additional_layout.addWidget(QLabel("Index Creation:"))
        additional_layout.addWidget(self.index_creation_combo)
        self.summary_per_section_combo = QComboBox()
        self.summary_per_section_combo.addItems(["true", "false"])
        additional_layout.addWidget(QLabel("Summary Per Section:"))
        additional_layout.addWidget(self.summary_per_section_combo)
        self.key_takeaways_combo = QComboBox()
        self.key_takeaways_combo.addItems(["end_of_guide", "none"])
        additional_layout.addWidget(QLabel("Key Takeaways:"))
        additional_layout.addWidget(self.key_takeaways_combo)
        self.protocol_adherence_combo = QComboBox()
        self.protocol_adherence_combo.addItems(["strict_ieee_standards", "general_guidelines"])
        additional_layout.addWidget(QLabel("Protocol Adherence:"))
        additional_layout.addWidget(self.protocol_adherence_combo)
        self.configuration_fineness_combo = QComboBox()
        self.configuration_fineness_combo.addItems(["granular_settings", "basic_settings"])
        additional_layout.addWidget(QLabel("Configuration Fineness:"))
        additional_layout.addWidget(self.configuration_fineness_combo)
        self.error_tolerance_combo = QComboBox()
        self.error_tolerance_combo.addItems(["minimal", "moderate"])
        additional_layout.addWidget(QLabel("Error Tolerance:"))
        additional_layout.addWidget(self.error_tolerance_combo)
        self.update_frequency_combo = QComboBox()
        self.update_frequency_combo.addItems(["real_time", "periodic", "none"])
        additional_layout.addWidget(QLabel("Update Frequency:"))
        additional_layout.addWidget(self.update_frequency_combo)
        self.accessibility_features_combo = QComboBox()
        self.accessibility_features_combo.addItems(["screen_reader_compatible", "none"])
        additional_layout.addWidget(QLabel("Accessibility Features:"))
        additional_layout.addWidget(self.accessibility_features_combo)
        self.multimedia_integration_combo = QComboBox()
        self.multimedia_integration_combo.addItems(["optional_videos", "none"])
        additional_layout.addWidget(QLabel("Multimedia Integration:"))
        additional_layout.addWidget(self.multimedia_integration_combo)
        self.data_privacy_combo = QComboBox()
        self.data_privacy_combo.addItems(["gdpr_compliant", "basic_privacy"])
        additional_layout.addWidget(QLabel("Data Privacy:"))
        additional_layout.addWidget(self.data_privacy_combo)
        self.scalability_considerations_combo = QComboBox()
        self.scalability_considerations_combo.addItems(["cloud_vs_on_premise", "none"])
        additional_layout.addWidget(QLabel("Scalability Considerations:"))
        additional_layout.addWidget(self.scalability_considerations_combo)
        self.interoperability_combo = QComboBox()
        self.interoperability_combo.addItems(["cross_platform", "single_platform"])
        additional_layout.addWidget(QLabel("Interoperability:"))
        additional_layout.addWidget(self.interoperability_combo)
        form_layout.addLayout(additional_layout)

        # Output and Buttons
        output_layout = QHBoxLayout()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)
        button_layout = QVBoxLayout()
        self.generate_button = QPushButton("Generate Prompt")
        self.generate_button.clicked.connect(self.generate_prompt)
        button_layout.addWidget(self.generate_button)
        self.save_button = QPushButton("Save as YAML")
        self.save_button.clicked.connect(self.save_as_yaml)
        button_layout.addWidget(self.save_button)
        output_layout.addLayout(button_layout)
        form_layout.addLayout(output_layout)

        main_layout.addLayout(form_layout)
        self.show()

    def generate_prompt(self):
        prompt = {
            "prompt": {
                "version": self.version_input.text(),
                "timestamp": self.timestamp_input.text(),
                "language": self.language_combo.currentText(),
                "language_strictness": self.language_strictness_combo.currentText(),
                "protocol_strictness": self.protocol_strictness_combo.currentText(),
                "context": {
                    "domain": self.domain_input.text(),
                    "subdomain": self.subdomain_input.text(),
                    "specific_topic": self.specific_topic_input.text(),
                    "geographical_scope": self.geographical_scope_input.text(),
                    "historical_period": self.historical_period_input.text()
                },
                "task": {
                    "type": self.task_type_combo.currentText(),
                    "goal": self.task_goal_input.text(),
                    "constraints": {
                        "word_limit": self.word_limit_input.text(),
                        "tone": self.tone_combo.currentText(),
                        "audience": self.audience_combo.currentText(),
                        "language_adherence": self.language_adherence_input.text(),
                        "technical_accuracy": self.technical_accuracy_input.text(),
                        "citation_requirement": self.citation_requirement_input.text()
                    }
                },
                "content": {
                    "main_question": self.main_question_input.toPlainText(),
                    "subquestions": [line.strip() for line in self.subquestions_input.toPlainText().split("\n") if line.strip()],
                    "examples": [json.loads(line.strip()) for line in self.examples_input.toPlainText().split("\n") if line.strip()],
                    "additional_resources": [line.strip() for line in self.additional_resources_input.toPlainText().split("\n") if line.strip()]
                },
                "response_format": {
                    "structure": self.structure_type_combo.currentText(),
                    "sections": [line.strip() for line in self.sections_input.toPlainText().split("\n") if line.strip()],
                    "output_type": self.output_type_combo.currentText(),
                    "format_consistency": self.format_consistency_input.text(),
                    "section_length": self.section_length_input.text(),
                    "cross_referencing": self.cross_referencing_input.text()
                },
                "feedback_mechanism": {
                    "expected": self.feedback_expected_combo.currentText(),
                    "format": self.feedback_format_combo.currentText(),
                    "fields": [line.strip() for line in self.feedback_fields_input.toPlainText().split("\n") if line.strip()],
                    "feedback_frequency": self.feedback_frequency_input.text()
                },
                "depth_level": self.depth_level_combo.currentText(),
                "max_tokens_usage": self.max_tokens_usage_combo.currentText(),
                "include_diagrams": self.include_diagrams_combo.currentText(),
                "historical_context": self.historical_context_combo.currentText(),
                "future_trends": self.future_trends_combo.currentText(),
                "case_studies": self.case_studies_combo.currentText(),
                "comparisons": self.comparisons_combo.currentText(),
                "glossary": self.glossary_combo.currentText(),
                "quizzes": self.quizzes_combo.currentText(),
                "references": self.references_combo.currentText(),
                "prerequisites": self.prerequisites_combo.currentText(),
                "interactivity_suggestions": self.interactivity_suggestions_combo.currentText(),
                "visual_aids": self.visual_aids_combo.currentText(),
                "error_handling": self.error_handling_combo.currentText(),
                "performance_metrics": self.performance_metrics_combo.currentText(),
                "ensure_no_english": self.ensure_no_english_combo.currentText(),
                "translation_check": self.translation_check_combo.currentText(),
                "term_consistency": self.term_consistency_combo.currentText(),
                "audience_adaptation": self.audience_adaptation_combo.currentText(),
                "section_transitions": self.section_transitions_combo.currentText(),
                "citation_style": self.citation_style_combo.currentText(),
                "index_creation": self.index_creation_combo.currentText(),
                "summary_per_section": self.summary_per_section_combo.currentText(),
                "key_takeaways": self.key_takeaways_combo.currentText(),
                "protocol_adherence": self.protocol_adherence_combo.currentText(),
                "configuration_fineness": self.configuration_fineness_combo.currentText(),
                "error_tolerance": self.error_tolerance_combo.currentText(),
                "update_frequency": self.update_frequency_combo.currentText(),
                "accessibility_features": self.accessibility_features_combo.currentText(),
                "multimedia_integration": self.multimedia_integration_combo.currentText(),
                "data_privacy": self.data_privacy_combo.currentText(),
                "scalability_considerations": self.scalability_considerations_combo.currentText(),
                "interoperability": self.interoperability_combo.currentText()
            }
        }
        self.output_text.setPlainText(json.dumps(prompt, indent=2, ensure_ascii=False))

    def save_as_yaml(self):
        prompt = json.loads(self.output_text.toPlainText())
        yaml_content = yaml.dump(prompt, allow_unicode=True, default_flow_style=False)
        file_name, _ = QFileDialog.getSaveFileName(self, "Save YAML File", "", "YAML Files (*.yml *.yaml)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(yaml_content)

def main():
    app = QApplication(sys.argv)
    ex = PromptGenerator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()