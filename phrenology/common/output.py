from abc import ABC, abstractmethod

class OutputAbstract(ABC):
    @abstractmethod
    def render_output(self, output_type, data = None):
        pass

    @abstractmethod
    def _render_counts(self, data):
        pass

    @abstractmethod
    def _render_list(self, data):
        pass

    @abstractmethod
    def _render_read(self, data):
        pass

    @abstractmethod
    def _render_error(self, data):
        pass
