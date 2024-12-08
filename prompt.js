<script>
    document.querySelectorAll('.prompt').forEach((prompt) => {
        prompt.addEventListener('click', () => {
            // Remove "selected" class from all prompts
            document.querySelectorAll('.prompt').forEach((p) => p.classList.remove('selected'));
            // Add "selected" class to the clicked prompt
            prompt.classList.add('selected');
        });
    });
</script>
